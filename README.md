# PyhomebridgeController
A python wrapper using the Homebridge UI API. 
# Accessories
| Method name | Arguments | Description |
| --- | --- | --- |
| `get_all_accessories` | None | Retrieves all accessories from Homebridge and returns a dictionary with all accessory information |
| `get_accessorie` | `uniqueId`: str | Retrieves an accessory using its `uniqueId` from Homebridge and returns a dictionary with all the accessory information |
| `get_layout` | None | Retrieves the layout of the accessories from Homebridge UI (user-dependent) and returns a dictionary with the layout of the accessories |
| `set_accessorie` | `uniqueId`: str, <br> `characteristicType`: str, <br> `value`: str | Sets a value to a characteristic of an accessory using its `uniqueId`, `characteristicType`, and `value`, and returns the old value of the characteristic |
| `get_characteristics` | `uniqueId`: str | Get all the characteristics of an accessory `{characteristics : value}` |



# Backup
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


# Child Bridge
| Method name | Arguments | Description |
| --- | --- | --- |
| restart_child | `childID`: str | Restart a child bridge. |
| stop_child | `childID`: str | Stop a child bridge. |
| start_child | `childID`: str | Start a child bridge. |
| get_status_child_bridges | None | Return a list of the active child bridges and their status. |


# Config
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



# Platform
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


# Plugins
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
| Method name | Arguments | Description |
| --- | --- | --- |
| get_users | None | Get a list of all users |
| create_user | `name`: str,<br> `username`: str,<br> `password`: str,<br> `admin`: bool` *(def "False")* | Create a new user |
| `update_user` | `id`: str,<br> `name`: str,<br> `username`: str, <br>`password`: str,<br> `admin`: bool *(def "False")* | Update an existing user |
| delete_user | `id`: str | Delete an existing user |
| change_user_password | `currentPassword`: str,<br> `newPassword`: str | Change the password of the current user |
| setup_otp | None | Setup the OTP for the current user |
| activate_otp | `otp`: str | Activate the OTP for the current user |
| deactivate_otp | None | Deactivate the OTP for the current user |


