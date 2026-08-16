from abc import ABC,abstractmethod
class Smartdevice(ABC):
    def show_device(self,name):
        print("Device name:",name)

    @abstractmethod
    def turn_on(self):
        pass

class Smartlight(Smartdevice):
    def turn_on(self):
        print("Smartlight is on")

class Smartfan(Smartdevice):
    def turn_on(self):
        print("Smartfan is on")

class Smartspeaker(Smartdevice):
    def turn_on(self):
        print("Smartspeaker is on")

class SmartTV(Smartdevice):
    def turn_on(self):
        print("SmartTV is on")

light=Smartlight()
fan=Smartfan()
speaker=Smartspeaker()
TV=SmartTV()

light.show_device("Living room light")
light.turn_on()

fan.show_device("Bedroom fan")
fan.turn_on()

speaker.show_device("Music speaker")
speaker.turn_on()

TV.show_device("TV")
TV.turn_on()
class Securitycamera:
    def check_status(self):
        print("Security camera is recording")

class Doorlock:
    def check_status(self):
        print("Door lock is secure")

devices=[Doorlock(), Securitycamera()]

print("")
print("=============Smart device status===============")
for device in devices:
    device.check_status()

print("===============================================")


