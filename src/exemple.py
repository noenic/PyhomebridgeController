# HB.Accessories.set_accessorie(HB.Accessories.accessories['stripe-e2f9dd'],"Saturation","80")
#HB.Accessories.set_accessorie(HB.Accessories.accessories['stripe-e2f9dd'],"On","0")
#print(HB.Server.set_mdns_advertiser("bonjour-hap"))

#print(HB.Plugins.search_plugins("yeelight"))
#print(HB.Plugins.lookup_plugin("homebridge-homematic"))
#print(HB.Plugins.lookup_plugin_version("homebridge-homematic"))
#print(HB.Plugins.get_changelog("homebridge-homematic"))
#print(HB.Plugins.get_latest_release("homebridge-homematic"))
#print(HB.Plugins.get_plugin_alias("homebridge-homematic"))
#print(HB.Config.get_plugin_config("homebridge-homematic"))
#print(HB.Config.replace_plugin_config("homebridge-homematic",[{"ccu_ip":"192.168.1.40"}]))
#print(HB.Config.enable_plugin("homebridge-homematic"))
#print(HB.Config.get_backups())
# print(HB.Config.get_backup("1671898776294"))
#print(HB.Users.setup_otp())
#print(HB.Users.activate_otp("792200"))
#print(HB.Users.deactivate_otp("password"))
#print(HB.Platform.restart_linux_host())
#print(HB.Platform.shutdown_linux_host())
#print(HB.Status.get_server_information())
#print(HB.Platform.get_docker_startup_script())
#print(HB.Platform.restart_docker_container())
#print(HB.Platform.get_startup_flags())
# print(HB.Platform.set_startup_flags({
#                     "HOMEBRIDGE_DEBUG": True,
#                     "HOMEBRIDGE_KEEP_ORPHANS": False,
#                     "HOMEBRIDGE_INSECURE": True,
#                     "ENV_DEBUG": "YES",
#                     "ENV_NODE_OPTIONS": "Probably"
#                     })
#                     )
#print(HB.Platform.set_startup_flags({"HOMEBRIDGE_INSECURE": True}))
#print(HB.Platform.set_full_service_restart_flag())
#print(HB.Platform.download_logs(colours="yes"))
#print(HB.Platform.clear_logs())
#print(HB.Backups.download_backup(filename="backup-2021.tar.gz",dir="/home/pi/"))
#print(HB.Backups.get_next_scheduled_backup())
#print(HB.Backups.get_generated_backups())
#print(HB.Backups.download_specific_backup("0ED441EDCF3F.1676600165689"))
#print(HB.Backups.trigger_backup_restore())
#print(HB.Backups.restore_from_hbfx("backup.hbfx"))