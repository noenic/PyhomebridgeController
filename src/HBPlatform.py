class HBPlatform:
    def __init__(self,HBController) -> None:
        self.HBController = HBController

    def get_platform_info(self)-> str:
        """Get the platform hosting information like if the host is a docker container or a linux host.

        Returns:
            str: The platform hosting information"""
        info=self.HBController.Status.get_server_information()
        if "homebridgeRunningInDocker" in info and info['homebridgeRunningInDocker']==True:
            return "Docker"
        elif "os" in info and info['os']["platform"]=="linux":
            return "Linux"
        else:
            return "Other platform"

    #-----------For Linux hosts (systemd)----------------
    def restart_linux_host(self):
        """Restart / reboot the host server.

        **Only available on Linux (systemd) hosts.**

        Returns:
            bool: True if the host is restarted"""
        platform=self.get_platform_info()   
        if platform!="Linux":
            raise Exception("This method is only available on Linux hosts, this is a "+self.get_platform_info()+" host")
        response= self.HBController.send_request("PUT","platform-tools/linux/restart-host").json()
        if "ok" in response:
            return True
        else:
            raise Exception(response['message'])

    
    def shutdown_linux_host(self):
        """Shutdown the host server.

        **Only available on Linux (systemd) hosts.**

        Returns:
            bool: True if the host is shutdown"""
        platform=self.get_platform_info()   
        if platform!="Linux":
            raise Exception("This method is only available on Linux hosts, this is a "+self.get_platform_info()+" host")
        response= self.HBController.send_request("PUT","platform-tools/linux/shutdown-host").json()
        if "ok" in response:
            return True
        else:
            raise Exception(response['message'])

    #-----------For Docker hosts----------------
    def get_docker_startup_script(self)-> dict:
        """Get the startup script for the Docker container.

        **Only available on Docker hosts.**

        Returns:
            dicts: The startup script"""
        platform=self.get_platform_info()   
        if platform!="Docker":
            raise Exception("This method is only available on Docker hosts, this is a "+self.get_platform_info()+" host")
        return self.HBController.send_request("GET","platform-tools/docker/startup-script").json()
         

    def set_docker_startup_script(self,script:str)-> bool:
        """Set the startup script for the Docker container.

        **Only available on Docker hosts.**
        **For some reason it's not working (error 500)**

        Args:
            script (str): The startup script

        Returns:
            bool: True if the script is set"""
        platform=self.get_platform_info()   
        if platform!="Docker":
            raise Exception("This method is only available on Docker hosts, this is a "+self.get_platform_info()+" host")
        return self.HBController.send_request("PUT","platform-tools/docker/startup-script",data=script).status_code==200
        



    def restart_docker_container(self):
        """Restart the Docker container.

        **Only available on Docker hosts.**

        Returns:
            bool: True if the container is restarted"""
        platform=self.get_platform_info()   
        if platform!="Docker":
            raise Exception("This method is only available on Docker hosts, this is a "+self.get_platform_info()+" host")
        return self.HBController.send_request("PUT","platform-tools/docker/restart-container").json()


    #-----------HB-service----------------

    def get_startup_flags(self)-> dict:
        """Return the startup flags and env variables for Homebridge.

        Returns:
            dict: The startup flags and env variables
        """
        return self.HBController.send_request("GET","platform-tools/hb-service/homebridge-startup-settings").json()



    def set_startup_flags(self,flags:dict)-> bool:
        """Set the startup flags and env variables for Homebridge.


        Args:
            flags (dict): The startup flags and env variables
            exemple: {
                    "HOMEBRIDGE_DEBUG": false,
                    "HOMEBRIDGE_KEEP_ORPHANS": false,
                    "HOMEBRIDGE_INSECURE": true,
                    "ENV_DEBUG": "string",
                    "ENV_NODE_OPTIONS": "string"
                    }

        Returns:
            bool: True if the flags are set
        """
        return self.HBController.send_request("PUT","platform-tools/hb-service/homebridge-startup-settings",data=flags).status_code==200


    def set_full_service_restart_flag(self):
        """Request the UI does a full restart next time a restart for Homebridge is sent.

        **When running under hb-service the UI will only restart if it detects it needs to.**

        Returns:
            bool: True if the flag is set
        """
        return self.HBController.send_request("PUT","platform-tools/hb-service/set-full-service-restart-flag").status_code==200


    def download_logs(self,colours="no")-> str:
        """Download the Homebridge logs.

        Returns:
            str: The Homebridge logs
        """
        return self.HBController.send_request("GET","platform-tools/hb-service/log/download?colour="+colours).content.decode("utf-8")


    def clear_logs(self)-> bool:
        """Clear the Homebridge logs.

        Returns:
            bool: True if the logs are cleared
        """
        return self.HBController.send_request("PUT","platform-tools/hb-service/log/truncate").status_code==200