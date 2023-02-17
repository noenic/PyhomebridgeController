
class HBStatus():
    def __init__(self,HBController) -> None:
        self.HBController = HBController

    def get_cpu_info(self)-> dict:
        """Return the current CPU load, load history and temperature (if available).

        Returns:
            dict: a dict with the cpu info"""
        return self.HBController.send_request("GET","status/cpu").json()
    

    def get_ram_info(self)-> dict:
        """Return total memory, memory usage, and memory usage history in bytes.

        Returns:
            dict: a dict with the ram info"""
        return self.HBController.send_request("GET","status/ram").json()

    def get_network_info(self)-> dict:
        """Returns the current transmitted & received bytes per second.

        Returns:
            dict: a dict with the network info"""
        return self.HBController.send_request("GET","status/network").json()

    def get_uptime(self)-> dict:
        """Return the host and process (UI) uptime..

        Returns:
            dict: a dict with the uptime info"""
        return self.HBController.send_request("GET","status/uptime").json()

    def get_status_homebridge(self)-> dict:
        """Return the current Homebridge status.

        Possible Homebridge statuses are up, pending or down.

        Returns:
            dict: a dict with the homebridge status info"""
        return self.HBController.send_request("GET","status/homebridge").json()

    
    def get_homebridge_version(self)-> dict:
        """Return the current Homebridge version / package information.

        Returns:
            dict: a dict with the homebridge version info"""
        return self.HBController.send_request("GET","status/homebridge-version").json()

    def get_server_information(self)-> dict:
        """Return the current server information.

        Returns:
            dict: a dict with the server information"""
        return self.HBController.send_request("GET","status/server-information").json()

    def get_nodejs_version(self)-> dict:
        """Return the current Node.js version.

        Returns:
            dict: a dict with the nodejs version info"""
        return self.HBController.send_request("GET","status/nodejs").json()


    def get_status_rpi_throttling(self)-> dict:
        """Return the current RPi throttling status.

        **This method is only supported on Raspberry Pi.**

        Returns:
            dict: a dict with the rpi throttling status info"""
        return self.HBController.send_request("GET","status/rpi/throttled").json()