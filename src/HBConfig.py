class HBConfig:
    def __init__(self,HBController) -> None:
        self.HBController = HBController

    def get_config(self)-> dict:
        """Get the config of Homebridge

        Returns:
            dict: a dict with the config of Homebridge"""
        return self.HBController.send_request("GET","config-editor").json()

    def rewrite_config(self,config:dict)-> dict:
        """Update the config of Homebridge the new config
        WARNING: THIS WILL OVERWRITE THE OLD CONFIG

        Args:
            config (dict): a dict with the new config

        Returns:
            dict: a dict with the new config"""
        return self.HBController.send_request("POST","config-editor",config).json()

    def get_plugin_config(self,pluginName:str)-> dict:
        """Return the config blocks for a specific plugin.

        Args:
            pluginName (str): the name of the plugin

        Returns:
            dict: a dict with the config of the plugin"""
        #TODO: check if the plugin exists

        if not pluginName in [plugin["name"] for plugin in self.HBController.Plugins.get_plugins()]:
            raise Exception("Plugin not found/installed")

        return self.HBController.send_request("GET","config-editor/plugin/"+pluginName).json()

    def replace_plugin_config(self,pluginName:str,config:list)-> dict:
        """Replace the config for a specific plugin.

        Args:
            pluginName (str): the name of the plugin e.g. "homebridge-config-ui-x"
            config (list): a list with a dict for each config block

        Returns:
            dict: a dict with the new config"""

        if not pluginName in [plugin["name"] for plugin in self.HBController.Plugins.get_plugins()]:
            raise Exception("Plugin not found/installed")
        
        return self.HBController.send_request("POST","config-editor/plugin/"+pluginName,config).json()
        

    def enable_plugin(self,pluginName:str)-> bool:
        """Mark the plugin as enable.

        Args:
            pluginName (str): the name of the plugin e.g. "homebridge-config-ui-x"

        Returns:
            bool: True if the plugin has been enabled
            """
        if not pluginName in [plugin["name"] for plugin in self.HBController.Plugins.get_plugins()]:
            raise Exception("Plugin not found/installed")
        
        return self.HBController.send_request("PUT","config-editor/plugin/"+pluginName+"/enable").status_code == 200

    def disable_plugin(self,pluginName:str)-> bool:
        """Mark the plugin as disable.

        Args:
            pluginName (str): the name of the plugin e.g. "homebridge-config-ui-x"

        Returns:
            bool: True if the plugin has been disabled
            """
        if not pluginName in [plugin["name"] for plugin in self.HBController.Plugins.get_plugins()]:
            raise Exception("Plugin not found/installed")
        
        return self.HBController.send_request("PUT","config-editor/plugin/"+pluginName+"/disable").status_code == 200


    
    def get_backups(self)-> list:
        """get the List of the available Homebridge config.json backups.

        Returns:
            list: a list of the backups"""
        return self.HBController.send_request("GET","config-editor/backups").json()

    def delete_backup(self)-> bool:
        """Delete all the Homebridge config.json backups.

        Returns:
            bool: True if the backups have been deleted"""
        return self.HBController.send_request("DELETE","config-editor/backups").status_code == 200


    def get_backup(self,backupID:str)-> dict:
        """Return the Homebridge config.json file for the given backup ID.

        Args:
            backupID (str): the id of the backup

        Returns:
            dict: a dict with the backup"""
        return self.HBController.send_request("GET","config-editor/backups/"+backupID).json()