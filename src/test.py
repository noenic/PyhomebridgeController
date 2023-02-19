from HBController import *
HB=HBController(username="username",password="password",IP_adress="xxx.xxx.xxx.xxx",port="8581",secure=False,otp=None,firstUser=False)

# secure = True if you use https (secure connection)
# otp = None if you don't use 2FA 
# firstUser = True if you want to create the first user (if the instance has not already been setup)
# Note that the username and password will be used to create the first user and return the same HBController object
# once the first user has been created, you can no longer use the firstUser argument







