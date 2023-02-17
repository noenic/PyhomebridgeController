
class HBAccessories:
    def __init__(self,HBController) -> None:
        self.HBController = HBController
        self.accessories= self.__get_link_names_to_uniqueids()


    #Get all accessories from Homebridge
    def get_all_accessories(self)-> dict:
        """Get all accessories from Homebridge

        Returns:
            dict: a dict with all the accessories"""
        return self.HBController.send_request("GET","accessories").json()


    #Get an accessory with its uniqueId from Homebridge
    def get_accessorie(self,uniqueId) -> dict:
        """
        Get an accessory with its uniqueId from Homebridge

        Args:
            uniqueId (str): the id of the accessory (e.g. "6bf697f14786eb03f9cf53c3f066feb46520bc801f1478b4818d7891c3cfd9d")
            
        Returns:
            dict: a dict with the information of the accessory"""
        return self.HBController.send_request("GET","accessories/"+uniqueId).json()

    def get_layout(self)-> dict:
        """Get the layout of the accessories from Homebridge UI (user dependant)
        
        Returns:
            dict: a dict with the layout of the accessories
        """
        return self.HBController.send_request("GET","accessories/layout").json()

    def set_accessorie(self,uniqueId:str,characteristicType:str,value:str)-> int:
        """
        Set a value to a characteristic of an accessory:
        Args:
            - uniqueId: the id of the accessory (e.g. "6bf697f14786eb03f9cf53c3f066feb46520bc801f1478b4818d7891c3cfd9d")
            - characteristicType: the type of the characteristic (e.g. "On" or "Brightness")
            - value: the value to set (e.g. 1 or 100 for a brightness, or true or false for a switch, 350 for a hue, 100 for a saturation)
        
        
        Returns:
            int: the old value of the characteristic"""
        response = self.HBController.send_request("PUT","accessories/"+uniqueId,{"characteristicType":characteristicType,"value":value})
        if response.status_code == 200:
            return response.json()["values"][characteristicType]

    #Get all accesories names and link them to their uniqueId 
    def __get_link_names_to_uniqueids(self) -> dict :
        """Get all accesories names and link them to their uniqueId
        
        Returns:
            dict: a dict with the name of the accessory as key and the uniqueId as value
        """
        accessories = self.get_all_accessories()
        accessories_with_uniqueId = {}
        for accessory in accessories:
            accessories_with_uniqueId[accessory["serviceName"]] = accessory["uniqueId"]
        return accessories_with_uniqueId

    def get_characteristics(self,uniqueId:str) -> dict:
        """Get all the characteristics of an accessory
        
        Args:
            uniqueId (str): the uniqueId of the accessory
        
        Returns:
            dict: a dict with the characteristics of the accessory
        """
        return self.get_accessorie(uniqueId)["values"]