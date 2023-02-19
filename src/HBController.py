from requests import get,post,put,delete,patch
#On enleve les warnings de requests (pour les certificats)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


from HBStatus import HBStatus
from HBChildBridge import HBChildBridge
from HBUsers import HBUsers
from HBAccessories import HBAccessories
from HBServer import HBServer
from HBConfig import HBConfig
from HBPlugins import HBPlugins
from HBPlatform import HBPlatform
from HBBackups import HBBackups

from datetime import datetime

class HBController:


        

    def __init__(self,username,password,IP_adress,port,secure=False,otp=None,firstUser=False) -> None:
        """Create a Homebridge Controler
        
        Args:
            - username (str): The username of the Homebridge UI
            - password (str): The password of the Homebridge UI
            - IP_adress (str): The IP adress of the Homebridge instance
            - port (str): The port of the Homebridge instance
            - secure (bool, optional): If the Homebridge instance is secure (https) or not. Defaults to False.
            - otp (str, optional): The 2FA code. Defaults to None.
            - firstUser (bool, optional): If the Homebridge instance has NOT ALREADY BEEN SETUP . Defaults to False. (If True, the username and password will be used to create the first user)

        """
        self.USERNAME = username
        self.__PASSWORD = password
        self.IP_ADRESS = IP_adress
        self.PROTOCOL = "https" if secure else "http"
        self.PORT = port
        self.BASE_URL = f"{self.PROTOCOL}://{self.IP_ADRESS}:{self.PORT}/api/"
        if firstUser:
            if self.create_first_user(username,password):
                print("First user created ! You can now use the username and password to connect to Homebridge")
            else:
                print("Could not create the first user :\n-- The instance has already been setup\n-- Password is too short (min 3 characters)\n\nRemove the firstUser=True argument to connect to an already setup instance ")


        self.__TOKEN=self.__get_token(otp) 

        self.Status=HBStatus(self)
        self.ChildBridge=HBChildBridge(self)
        self.Users=HBUsers(self,password)
        self.Accessories=HBAccessories(self)
        self.Server=HBServer(self)
        self.Config=HBConfig(self)
        self.Plugins=HBPlugins(self)
        self.Platform=HBPlatform(self)
        self.Backups=HBBackups(self)

    def create_first_user(self,username:str,password:str)-> dict:
        """Create the first user of the Homebridge instance (Only if the instance has NOT ALREADY BEEN SETUP)
            The user will be an admin and will have the name "Admin" (You can change it later)
        
        Args:
            - username (str): The username of the user
            - password (str): The password of the user
        
        Returns:
            dict: The response of the request
        """
        reponse=post(self.BASE_URL+"setup-wizard/create-first-user",json={"name":"Admin","username":username,"password":password,"admin":True},verify=False)
        return reponse.status_code==201




    def __get_token(self,otp=None)-> dict:
        """Get a token from Homebridge API

        Returns:
            dict: a dict with the token and the expire_at timestamp

        Raises:
            Exception: If the username or password is wrong
        """
        json={"username": self.USERNAME, "password": self.__PASSWORD}
        if otp:
            json["otp"]=otp
        response = post(self.BASE_URL + "auth/login", json=json,verify=False).json()
        if "access_token" in response:
            return {"token":response['access_token'],"expire_at" :datetime.now().timestamp()+int(response['expires_in'])}
        else:
            raise Exception(response['message']+" (Probably wrong username or password or 2FA enabled)")

    def __check_token_validity(self)-> None:
        """Check if the token is valid by comparing the expire_at timestamp with the current timestamp"""
        if self.__TOKEN["expire_at"] < datetime.now().timestamp():
            self.__TOKEN=self.__get_token()

    def check_token(self)-> bool:
        """Check if the token is valid via the Homebridge API
        
        Returns:
            bool: True if the token is valid, False if not
        """
        response=get(self.BASE_URL + "auth/check", headers={"Authorization": "Bearer " + self.__TOKEN["token"]})
        if response.json()["status"]=="OK":
            return True
        else:
            return False
    
    def send_request(self,method:str,path:str,data:dict=None,files=None) -> dict:
        """Send a request to Homebridge API
        
        Args:
            - method (str): The method of the request (GET,POST,PUT,DELETE,PATCH)
            - path (str): The path of the request (ex: "server/status")
            - data (dict, optional): The data to send. Defaults to None.
        
        Returns:
            dict: The response of the request
        
        Raises:

            Exception: If the method is not valid
            Exception: If the request return an error
            """
        self.__check_token_validity()
        if method == "GET":
            response = get(self.BASE_URL + path, headers={"Authorization": "Bearer " + self.__TOKEN["token"]},verify=False)
        elif method == "POST":
            response=  post(self.BASE_URL + path, headers={"Authorization": "Bearer " + self.__TOKEN["token"]},json=data,files=files,verify=False)
        elif method == "PUT":
            response = put(self.BASE_URL + path, headers={"Authorization": "Bearer " + self.__TOKEN["token"]},json=data,verify=False)
        elif method == "DELETE":
            response =  delete(self.BASE_URL + path, headers={"Authorization": "Bearer " + self.__TOKEN["token"]},verify=False)
        elif method == "PATCH":
            response = patch(self.BASE_URL + path, headers={"Authorization": "Bearer " + self.__TOKEN["token"]},json=data,verify=False)
        else:
            raise Exception("Invalid method")
        if response.status_code in [200,201,202,203,204]:
            return response

        elif response.status_code in [401]:
            if not self.check_token():
                print("Token is not valid anymore, we will try to get a new one")
                self.__TOKEN=self.__get_token()
                return self.send_request(method,path,data)
                
        else:
            if response.status_code in [404] :
                raise Exception("The path {0} is not valid, Nothing found {1}".format(path,response.status_code,))
            raise Exception(response.status_code,response.json())






