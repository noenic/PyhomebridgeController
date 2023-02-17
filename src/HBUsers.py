
class HBUsers:
    def __init__(self,HBController,password) -> None:
        self.HBController = HBController
        self.__PASSWORD = password


    def get_users(self)-> list:
        """Get a list of all users

        Returns:
            list: a list of dict with the users info"""
        return self.HBController.send_request("GET","users").json()

    def create_user(self,name:str,username:str,password:str,admin:bool=False)-> dict:
        """Create a new user

        Args:
            - name (str): The name of the user
            - username (str): The username of the user
            - admin (bool): If the user is an admin or not (default: False)
            - password (str): The password of the user

        Returns:
            dict: a dict with the user info"""
        return self.HBController.send_request("POST","users",{"name":name,"username":username,"admin":admin,"password":password}).json()


    def update_user(self,id:str,name:str,username:str,password:str,admin:bool=False)-> dict:
        """Update an existing user

        Args:
            - id (str): The id of the user
            - name (str): The name of the user
            - username (str): The username of the user
            - admin (bool): If the user is an admin or not (default: False)
            - password (str): The password of the user

        Returns:
            dict: a dict with the user info"""
        return self.HBController.send_request("PATCH","users/"+id,{"name":name,"username":username,"admin":admin,"password":password}).json()


    def delete_user(self,id:str)-> dict:
        """Delete an existing user

        Args:
            - id (str): The id of the user

        Returns:
            dict: a dict with the user info"""
        if self.HBController.send_request("DELETE","users/"+id).status_code==200:
            return {"status":"OK"}
        else:
            return {"status":"could not delete user"}


    def change_user_password(self,currentPassword:str,newPassword:str)-> dict:
        """Change the password of the current user

        Args:
            - currentPassword (str): The current password of the user
            - newPassword (str): The new password of the user

        Returns:
            dict: a dict with the user info"""
        return self.HBController.send_request("POST","users/change-password",{"currentPassword":currentPassword,"newPassword":newPassword}).json()
        


    def setup_otp(self)-> dict:
        """Setup the OTP for the current user

        Returns:
            dict: a dict with the user info"""
        return self.HBController.send_request("POST","users/otp/setup").json()

    def activate_otp(self,otp:str)-> dict:
        """Activate the OTP for the current user

        Args:
            - otp (str): The OTP code

        Returns:
            dict: a dict with the user info"""
        return self.HBController.send_request("POST","users/otp/activate",{"code":otp}).json()

    def deactivate_otp(self)-> dict:
        """Deactivate the OTP for the current user

        Args:
            - password (str): The password of the user

        Returns:
            dict: a dict with the user info"""
        return self.HBController.send_request("POST","users/otp/deactivate",{"password":self.__PASSWORD}).json()