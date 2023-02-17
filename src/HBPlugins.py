class HBPlugins:
    def __init__(self, HBController) -> None:
        self.HBController = HBController

    def get_plugins(self) -> list:
        """Get a List of currently installed Homebridge plugins.

        Returns:
            list: a list with all plugins"""
        return self.HBController.send_request("GET", "plugins").json()

    def search_plugins(self, query: str) -> list:
        """Search the NPM registry for Homebridge plugins.

        Args:
            query (str): the query to search for

        Returns:
            list: a list with all plugins"""
        return self.HBController.send_request("GET", "plugins/search/" + query).json()
    
    def lookup_plugin(self, name: str) -> dict:
        """Lookup a single plugin from the NPM registry.

        Args:
            name (str): the name of the plugin e.g. "homebridge-config-ui-x"
        Returns:
            dict: a dict with the plugin info"""
        return self.HBController.send_request("GET", "plugins/lookup/" + name).json()

    def lookup_plugin_version(self, name: str) -> dict:
        """Get the available versions and tags for a single plugin from the NPM registry.

        Args:
            name (str): the name of the plugin e.g. "homebridge-config-ui-x"
            version (str): the version of the plugin e.g. "4.41.0"
        Returns:
            dict: a dict with the plugin versions"""
        return self.HBController.send_request("GET", "plugins/lookup/" + name + "/versions").json()

    

    def get_config_schema(self, name: str) -> dict:
        """Get the config schema for a plugin.

        Args:
            name (str): the name of the plugin e.g. "homebridge-config-ui-x"

        Returns:
            dict: a dict with the config schema"""
        return self.HBController.send_request("GET", "plugins/config-schema/" + name).json()

    
    def get_changelog(self, name: str) -> dict:
        """Get the changelog for a plugin.

        Args:
            name (str): the name of the plugin e.g. "homebridge-config-ui-x"

        Returns:
            dict: a dict with the changelog"""
        return self.HBController.send_request("GET", "plugins/changelog/" + name).json()

    def get_latest_release(self, name: str) -> dict:
        """Get the latest release for a plugin.

        Args:
            name (str): the name of the plugin e.g. "homebridge-config-ui-x"

        Returns:
            dict: a dict with the latest release"""
        return self.HBController.send_request("GET", "plugins/release/" + name).json()

    
    def get_plugin_alias(self, name: str) -> dict:
        """Get the alias and type for a plugin.

        Args:
            name (str): the name of the plugin e.g. "homebridge-config-ui-x"

        Returns:
            dict: a dict with the alias and type if it exists"""
        return self.HBController.send_request("GET", "plugins/alias/" + name).json()


    