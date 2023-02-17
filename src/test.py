from HBController import *
HB=HBController(username="username",password="password",IP_adress="xxx.xxx.xxx.xxx",port="8581",secure=False,otp=None,firstUser=False)

#Accessories
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
print(HB.Accessories.set_accessorie("da02010c7c04998675990eacffcb3499b34bab66aac880b036787414bbb5d92b","On",1)) #Turn on the light


#Let's try to change the color of the light to green using the Hue and Saturation characteristics
print(HB.Accessories.set_accessorie(light,"Hue",120)) #Set the Hue to 120°
print(HB.Accessories.set_accessorie(light,"Saturation",100)) #Set the Saturation to 100%







