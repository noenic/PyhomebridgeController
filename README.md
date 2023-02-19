# PyhomebridgeController
A python wrapper using the Homebridge UI API.

- You can use this library to control your Homebridge UI instance from python.<br>
- You will need to have the Homebridge UI installed on your Homebridge instance and the -I flag enabled.<br>
- Use your UI credentials to login, you can also create the first user with this library.
```py
from HBController import *
HB=HBController(username="username",password="password",IP_adress="xxx.xxx.xxx.xxx",port="8581",secure=False,otp=None,firstUser=False)

# secure = True if you use https (secure connection)
# otp = None if you don't use 2FA 
# firstUser = True if you want to create the first user (if the instance has not already been setup)
# Note that the username and password will be used to create the first user and return the same HBController object
# once the first user has been created, you can no longer use the firstUser argument 

#You can then access the submodules like this:
HB.Plugins.method()
HB.Config.method()
HB.Accessories.method()
HB.Users.method()
#etc...
```




# Accessories
You can use the class HBAccessories to get all the accessories and their informations, or to change the value of a characteristic of an accessory.
- You will need to know the uniqueId of the accessory you want to access, you can get it with the method `get_all_accessories` or if you know the name of the accessory you can use the attribute `accessories` which is a dict with the name of the accessory as key and the uniqueId as value.<br>

| Method name | Arguments | Description |
| --- | --- | --- |
| `get_all_accessories` | None | Retrieves all accessories from Homebridge and returns a dictionary with all accessory information |
| `get_accessorie` | `uniqueId`: str | Retrieves an accessory using its `uniqueId` from Homebridge and returns a dictionary with all the accessory information |
| `get_layout` | None | Retrieves the layout of the accessories from Homebridge UI (user-dependent) and returns a dictionary with the layout of the accessories |
| `set_accessorie` | `uniqueId`: str, <br> `characteristicType`: str, <br> `value`: str | Sets a value to a characteristic of an accessory using its `uniqueId`, `characteristicType`, and `value`, and returns the old value of the characteristic |
| `get_characteristics` | `uniqueId`: str | Get all the characteristics of an accessory `{characteristics : value}` |

```py
#Get all accessories and their informations (dict)
print(HB.Accessories.get_all_accessories())  

#Get the arrangement of the accessories in the virtual rooms of Homebridge
print(HB.Accessories.get_layout())

#Get the informations of a specific accessory (dict) with  its id
print(HB.Accessories.get_accessorie("da02010c7c04998675990eacffcb3499b34bab66aac880b036787414bbb5d92b"))

#For easier use, the class HBAccessories has an attribute "accessories" which is a dict with the name of the accessory as key and the uniqueId as value
light=HB.Accessories.accessories['stripe-e2f9dd'] #= da02010c7c04998675990eacffcb3499b34bab66aac880b036787414bbb5d92b

#Get the characteristics of an accessory
print(HB.Accessories.get_characteristics(light).keys()) # The characteristics is the key and the value is the current value of the characteristic
#for this light the characteristics are: ['On', 'Brightness', 'Hue', 'Saturation', 'ColorTemperature', 'SupportedCharacteristicValueTransitionConfiguration', 'CharacteristicValueTransitionControl', 'CharacteristicValueActiveTransitionCount']
#This doesn't mean we can change all of them, for example we can't change the CharacteristicValueTransitionControl

#Let's try to turn on the light
print(HB.Accessories.set_accessorie(light,"On",1)) #Turn on the light


#Let's try to change the color of the light to green using the Hue and Saturation characteristics
print(HB.Accessories.set_accessorie(light,"Hue",120)) #Set the Hue to 120°
print(HB.Accessories.set_accessorie(light,"Saturation",100)) #Set the Saturation to 100%
```
**Note that every accessory available in homebridge is accessible and controllable here**<br>
**Also note that the characteristics are not the same for every accessory, for example the light doesn't have a "TargetTemperature" characteristic, like a thermostat does.**<br>



# Backup
The class HBBackup allows you to manage the backups of your Homebridge instance. You can download, upload,restore backups, and get the next scheduled backup.

| Method name | Arguments | Description |
| --- | --- | --- |
| `download_backup` | `filename` : str *(def : "Backup")*<br>`dir`: str *(def : ".")* | Download a .tar.gz of the Homebridge instance |
| `get_next_scheduled_backup` |None | Return the date and time of the next scheduled backup |
| `get_generated_backups` | None| Return the generated backups from the system |
| `download_specific_backup` | `id`: str,<br> `filename`: str *(def : "Backup")*,<br> `dir`:str *(def : ".")* | Download a system generated instance backup |
| `upload_backup` | `path`: str | Upload a .tar.gz of the Homebridge instance |
| `trigger_backup_restore` |None | Triggers a headless restore process from the last uploaded backup file |
| `restore_from_hbfx` | `path`:str | Upload a .hbfx backup file created by third party apps |
| `hard_restart_after_restore` | None | Trigger a hard restart of Homebridge (use after restoring backup) |
```py
#You can make a current backup of your Homebridge instance, and download it to your local machine.
#You can set a custom filename for the backup, or leave it blank to use the default filename.
#You can also set a custom directory to save the backup to, or leave it blank to save it to the current working directory.
print(HB.Backups.download_backup(filename="backup-2021.tar.gz",dir="/home/pi/"))


#You can get the next scheduled backup time 
print(HB.Backups.get_next_scheduled_backup())


#You can get all the backups that have been generated by Homebridge Config UI X
print(HB.Backups.get_generated_backups())

#After that you can download a specific backup by passing the backup ID.

print(HB.Backups.download_specific_backup(id="0E341EEC85C2.1676677018741",filename="backup-2021.tar.gz",dir="/home/pi/"))

#You can upload a backup to Homebridge Config UI X
# /!\ This will overwrite the current Homebridge instance with the backup you upload. (credentials, plugins, config.json, etc.)/!\
# /!\ Also note that it doesn't work for now (bug in the API) /!\
print(HB.Backups.upload_backup("/home/pi/backup-2021.tar.gz"))

#Once you have uploaded a backup, you can trigger a restore from the backup you uploaded.
print(HB.Backups.trigger_backup_restore())

#You can also restore a backup from HOOBS format (hbfx) by passing the path to the backup file.
print(HB.Backups.restore_from_hbfx("/home/pi/backup-2021.hbfx"))
```


# Child Bridge
The class HBChildBridge allows you to manage the child bridges of your Homebridge instance. You can restart, stop, start, and get the status of the child bridges.
- You will need to know the id of the child bridge you want to access. <br>
by default it's the MAC address of the child bridge. You can change the username in the config.json file <br>

| Method name | Arguments | Description |
| --- | --- | --- |
| restart_child | `childID`: str | Restart a child bridge. |
| stop_child | `childID`: str | Stop a child bridge. |
| start_child | `childID`: str | Start a child bridge. |
| get_status_child_bridges | None | Return a list of the active child bridges and their status. |
```py
#Get all the information about the child bridges 
print(HB.ChildBridge.get_status_child_bridges())

#Restart a child bridge using its id (its the 'username' key in the dictionary returned by the previous function)
print(HB.ChildBridge.restart_child("0E:8C:DA:AE:3A:5D"))

#Stop a child bridge
print(HB.ChildBridge.stop_child("0E:8C:DA:AE:3A:5D"))

#Start a child bridge
print(HB.ChildBridge.start_child("0E:8C:DA:AE:3A:5D"))
```


# Config
The class HBConfig allows you to manage the config of your Homebridge instance. You can get the config, rewrite the config, get the config of a specific plugin, replace the config of a specific plugin, enable or disable a plugin, get the backups, delete the backups, and get a specific backup.
- Be careful, I sugest you to use the method `get_config` to get the config, and then use the method `rewrite_config` to rewrite the config. to be extra safe. <br>
- You will need to know the real name of the plugin you want to access. <br>
for example, the plugin `Homebridge UI ` is actually called `homebridge-config-ui-x` on the NPM registry. <br>

| Method name | Arguments | Description |
| --- | --- | --- |
| get_config | None | Get the config of Homebridge |
| rewrite_config | `config`: dict | Update the config of Homebridge the new config<br>**WARNING: THIS WILL OVERWRITE THE OLD CONFIG** |
| get_plugin_config | `pluginName`: str | Return the config blocks for a specific plugin. |
| replace_plugin_config | `pluginName`: str,<br> `config`: list | Replace the config for a specific plugin. |
| enable_plugin | `pluginName`: str | Mark the plugin as enable. |
| disable_plugin | `pluginName`: str | Mark the plugin as disable. |
| get_backups | None | get the List of the available Homebridge config.json backups. |
| delete_backup | None | Delete all the Homebridge config.json backups. |
| get_backup | `backupID`: str | Return the Homebridge config.json file for the given backup ID. |
```py
#Get the config.json file of your homebridge instance
print(HB.Config.get_config())

#Rewrite the config.json file of your homebridge instance
print(HB.Config.rewrite_config({"bridge":{"name":"Homebridge","username":"0E:4D:4A:CE:0E:4D","port":51826,"pin":"031-45-154"},"description":"Homebridge","platforms":[{"platform":"Nest","name":"Nest"}]}))

#Get the config section of a plugin (plugin needs to be installed)
print(HB.Config.get_plugin_config("homebridge-yeelight-wifi"))

#Replace the config section of a plugin (plugin needs to be installed)
print(HB.Config.replace_plugin_config("homebridge-yeelight-wifi",[{"platform":"yeelight","name":"Yeelight","disableDeviceDiscovery":True,"devices":[{"name":"Yeelight","ip":"xxx.xxx.xxx.xxx","model":"ceiling4","disableAutomaticLightDetection":True}]}]))

#Enable/Disable a plugin (plugin needs to be installed)
print(HB.Config.enable_plugin("homebridge-yeelight-wifi"))
print(HB.Config.disable_plugin("homebridge-yeelight-wifi"))

#Homebridge will make automatic backups of your config.json file. You can get a list of all backups here and get their ids
print(HB.Config.get_backups())

#Then you can get the config.json content of a specific backup
print(HB.Config.get_backup("1676756544816"))

#Delete all backups stored on your homebridge instance
print(HB.Config.delete_backup())

#A backup will be made everytime you change the config.json file. So if you want to save your current config.json file you can do it like this
#It will simply rewrite the config.json file with the same content (so it will make a backup)
print(HB.Config.rewrite_config(HB.Config.get_config()))
```



# Platform
The class HBPlatform allows you to manage the platform of your Homebridge instance. You can get the platform info, restart, shutdown, get the startup script, set the startup script, restart the docker container, get the startup flags, set the startup flags, and set the full service restart flag.
- These methods are platform specific, so if you are using a docker container, you can't use the methods for the linux host. and vice versa. <br>

| Method name | Arguments | Description |
| --- | --- | --- |
| get_platform_info | None | Get the platform hosting information |
| restart_linux_host | None | Restart / reboot the host server. <br>**Only available on Linux (systemd) hosts.** |
| shutdown_linux_host | None | Shutdown the host server. <br>**Only available on Linux (systemd) hosts.** |
| get_docker_startup_script | None | Get the startup script for the Docker container.  <br>**Only available on Docker hosts.** |
| set_docker_startup_script | `script`: str | Set the startup script for the Docker container. <br>**Only available on Docker hosts.** |
| restart_docker_container | None | Restart the Docker container. <br>**Only available on Docker hosts.** |
| get_startup_flags | None | Return the startup flags and env variables for Homebridge. |
| set_startup_flags | `flags`: dict | Set the startup flags and env variables for Homebridge. |
| set_full_service_restart_flag | None | Request the UI to perform a full service restart. |

```py
#You can use the following commands to restart or shutdown the host system:
#On Linux Hosts
print(HB.Platform.restart_linux_host())
print(HB.Platform.shutdown_linux_host())

#On Docker Hosts
print(HB.Platform.restart_docker_container())

#This will return the startup script for the docker container.
print(HB.Platform.get_docker_startup_script())

#You can set the startup script for the docker container with the following command: be careful, this will overwrite the current startup script.
print(HB.Platform.set_docker_startup_script("apt-get update && apt-get install -y python3"))

#Get the startup flags for the Homebridge service (like HOMEBRIDGE_INSECURE -I)
print(HB.Platform.get_startup_flags())

#Set the startup flags for the Homebridge service
#This will overwrite the current startup flags, be careful!
print(HB.Platform.set_startup_flags({
                    "HOMEBRIDGE_DEBUG": True,
                    "HOMEBRIDGE_KEEP_ORPHANS": False,
                    "HOMEBRIDGE_INSECURE": True,
                    "ENV_DEBUG": "YES",
                    "ENV_NODE_OPTIONS": "Probably"
                    })
    )

#Let's turn it back to normal
print(HB.Platform.set_startup_flags({"HOMEBRIDGE_INSECURE": True}))

#Request the UI to perform a full service restart. (I don't know what it actually does)
print(HB.Platform.set_full_service_restart_flag())

#Get the logs from the Homebridge console, with or without colours (yes/no)
print(HB.Platform.download_logs(colours="yes"))

#Clear the logs from the Homebridge console
print(HB.Platform.clear_logs())
```


# Plugins
The class HBPlugins allows you to manage the plugins of your Homebridge instance. You can get the plugins, search for plugins, lookup a plugin, lookup a plugin version, get the config schema, get the changelog, get the latest release, and get the plugin alias.
- You will need to know the real name of the plugin you want to access. <br>
for example, the plugin `Homebridge UI ` is actually called `homebridge-config-ui-x` on the NPM registry. <br>

| Method name | Arguments | Description |
| --- | --- | --- |
| get_plugins | None | Get a list of currently installed Homebridge plugins. |
| search_plugins | `query`: str | Search the NPM registry for Homebridge plugins. |
| lookup_plugin | `name`: str | Lookup a single plugin from the NPM registry. |
| lookup_plugin_version | `name`: str | Get the available versions and tags for a single plugin from the NPM registry. |
| get_config_schema | `name`: str | Get the config schema for a plugin. |
| get_changelog | `name`: str | Get the changelog for a plugin. |
| get_latest_release | `name`: str | Get the latest release for a plugin. |
| get_plugin_alias | `name`: str | Get the alias and type for a plugin. |

# Server
The class HBServer allows you to manage the server of your Homebridge instance.
- Its like the settings page in the UI. <br>

| Method name | Arguments | Description |
| --- | --- | --- |
| restart_server | None | Restart the homebridge service |
| reset_homebridge_accessory | None | Unpair / Reset the Homebridge instance and remove cached accessories. |
| reset_cached_accessories | None | Remove Homebridge cached accessories. <br>**This method is only available when running hb-service.** |
| get_cached_accessories | None | Get the List cached Homebridge accessories. |
| delete_cached_accessory | `uuid`: str,<br>`cachefile`: str | Remove a single Homebridge cached accessory. <br>**This method is only available when running hb-service.** |
| get_pairing_list | None | Get List of all paired accessories (main bridge, external cameras, TVs etc). |
| get_pairing_of | `deviceID`: str | Get the pairing information of a specific accessory. |
| get_random_new_port | None | Get a random new port number unused. |
| get_system_interfaces | None | Get a list of available network interfaces on the server. |
| get_homebridge_interfaces | None | Get a list of available network interfaces that can be used by Homebridge. |
| set_interfaces | `interfaces`: list | Set the network interfaces that Homebridge will use. <br>**NEED TO BE RESTARTED TO DETECTED** |
| get_mdns_advertiser | None | Get the mDNS advertiser used by Homebridge. |
| set_mdns_advertiser | `advertiser`: str | Set the mDNS advertiser used by Homebridge. <br>**NEED TO BE RESTARTED TO DETECTED** |

# Status
The class HBStatus allows you to get the status of your Homebridge instance.
- Depending on your platform you will get different information. <br>
For example, if you are running Homebridge in a VM, you will not get the CPU temperature. <br>


| Method name | Arguments | Description |
| --- | --- | --- |
| get_cpu_info | None | Return the current CPU load, load history and temperature (if available). |
| get_ram_info | None | Return total memory, memory usage, and memory usage history in bytes. |
| get_network_info | None | Returns the current transmitted & received bytes per second. |
| get_uptime | None | Return the host and process (UI) uptime. |
| get_status_homebridge | None | Return the current Homebridge status. Possible Homebridge statuses are up, pending or down. |
| get_homebridge_version | None | Return the current Homebridge version / package information. |
| get_server_information | None | Return the current server information. |
| get_nodejs_version | None | Return the current Node.js version. |
| get_status_rpi_throttling | None | Return the current RPi throttling status.<br>**This method is only supported on Raspberry Pi**. |

# Users
The class HBUsers allows you to manage the users of your Homebridge instance.
- Be careful with the OTP methods, you can lock yourself out of the UI if you don't setup the OTP correctly. <br>

| Method name | Arguments | Description |
| --- | --- | --- |
| get_users | None | Get a list of all users |
| create_user | `name`: str,<br> `username`: str,<br> `password`: str,<br> `admin`: bool` *(def "False")* | Create a new user |
| update_user | `id`: str,<br> `name`: str,<br> `username`: str, <br>`password`: str,<br> `admin`: bool *(def "False")* | Update an existing user |
| delete_user | `id`: str | Delete an existing user |
| change_user_password | `currentPassword`: str,<br> `newPassword`: str | Change the password of the current user |
| setup_otp | None | Setup the OTP for the current user |
| activate_otp | `otp`: str | Activate the OTP for the current user |
| deactivate_otp | None | Deactivate the OTP for the current user |


