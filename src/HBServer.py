
class HBServer:
    def __init__(self, HBController) -> None:
        self.HBController = HBController

    def restart_server(self) -> bool:
        """Restart the homebridge service

        Returns:
            bool: True if the service is restarted"""

        return "ok" in self.HBController.send_request("PUT", "server/restart").json()


    #TODO: TEST THIS METHOD (i don't want to reset my homebridge instance)
    def reset_homebridge_accessory(self) -> bool:
        """Unpair / Reset the Homebridge instance and remove cached accessories.

        Returns:
            bool: True if the homebridge accessory is reset"""
        return "ok" in self.HBController.send_request("PUT", "server/reset").json()

    #TODO: TEST THIS METHOD (i don't want to reset my homebridge instance)
    def reset_cached_accessories(self) -> bool:
        """Remove Homebridge cached accessories.

        **This method is only available when running hb-service.**

        Returns:
            bool: True if the cached accessories are removed"""
        return "ok" in self.HBController.send_request("PUT", "server/reset/cached").json()

    #TODO: TEST THIS METHOD (i don't want to reset my homebridge instance)
    def get_cached_accessories(self) -> list:
        """Get the List cached Homebridge accessories.

        Returns:
            list: a list of the cached accessories"""
        return self.HBController.send_request("GET", "server/cached-accessories").json()


    #TODO: TEST THIS METHOD (i don't want to reset my homebridge instance)
    def delete_cached_accessory(self, uuid: str,cachefile:str) -> bool:
        """Remove a single Homebridge cached accessory.

        **This method is only available when running hb-service.**

        Args:
            uuid (str): The accessory UUID
            cachefile (str): The accessory cache file

        Returns:
            bool: True if the cached accessory is deleted"""
        return "ok" in self.HBController.send_request("DELETE", "server/cached-accessories/"+uuid+"?cacheFile="+cachefile).json()


    def get_pairing_list(self) -> list:
        """Get List of all paired accessories (main bridge, external cameras, TVs etc).

        Returns:
            list: a list of the paired devices"""
        return self.HBController.send_request("GET", "server/pairing").json()


    def get_pairing_of(self, deviceID: str) -> dict:
        """Get the pairing information of a specific accessory.

        Args:
            deviceID (str): The accessory ID

        Returns:
            dict: the pairing information of the accessory"""
        return self.HBController.send_request("GET", "server/pairing/"+deviceID).json()

    def get_random_new_port(self) -> int:
        """Get a random new port number unused.

        Returns:
            int: the new port number"""
        return self.HBController.send_request("GET", "server/port/new").json()

    def get_system_interfaces(self) -> list:
        """Get a list of available network interfaces on the server..

        Returns:
            list: the network interfaces of the system"""
        return self.HBController.send_request("GET", "server/network-interfaces/system").json()

    
    def get_homebridge_interfaces(self) -> list:
        """Get a list of available network interfaces that can be used by Homebridge.

        Returns:
            list: the network interfaces of the system that can be used by homebridge"""
        return self.HBController.send_request("GET", "server/network-interfaces/bridge").json()

    def set_interfaces(self, interfaces: list) -> bool:
        """Set the network interfaces that Homebridge will use.

        **NEED TO BE RESTARTED TO DETECTED**

        Args:
            interface (list): A list of network interfaces

        Returns:
            bool: True if the interfaces are set"""
        #We need to check if the interfaces are valid before sending the request (Homebridge will not check it)
        valid_interfaces =  [iface["iface"] for iface in self.get_system_interfaces()]
        if not all([iface in valid_interfaces for iface in interfaces]):
            raise ValueError("One or more interfaces are not valid")
        return self.HBController.send_request("PUT", "server/network-interfaces/bridge", {"adapters": interfaces}).status_code == 200

    def get_mdns_advertiser(self) -> str:
        """Get the mDNS advertiser used by Homebridge.

        Returns:
            str: the mDNS advertiser"""
        return self.HBController.send_request("GET", "server/mdns-advertiser").json()

    def set_mdns_advertiser(self, advertiser: str) -> bool:
        """Set the mDNS advertiser used by Homebridge.

        **NEED TO BE RESTARTED TO DETECTED**

        Args:
            advertiser (str): The mDNS advertiser

        Returns:
            bool: True if the mDNS advertiser is set"""
        return self.HBController.send_request("PUT", "server/mdns-advertiser", {"advertiser": advertiser}).status_code == 200

        