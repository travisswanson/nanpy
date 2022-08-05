from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)
#from nanpy.arduinoboard import setcomport

class DallasTemperature(ArduinoObject):
    cfg_h_name = 'USE_DallasTemperature'

    comportname = 'COM3'

    def __init__(self, pin, comportname, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.pin = pin
        self.comportname = comportname
        self.id = self.call('new', pin)

    @arduinoobjectmethod
    def setResolution(self, bits):
        pass

    @arduinoobjectmethod
    def setComPort(self, comPort):
        pass

    @returns(int)
    @arduinoobjectmethod
    def getResolution(self, bits):
        pass

    @returns(int)
    @arduinoobjectmethod
    def getDeviceCount(self):
        pass

    @arduinoobjectmethod
    def getAddress(self, index):
        val = self.call('getAddress')
        if val == "1":
            return val
        return val.split(' ')


    @arduinoobjectmethod
    def requestTemperatures(self, address_or_index = None):
        pass

    @returns(float)
    @arduinoobjectmethod
    def getTempC(self, address_or_index):
        pass

    @returns(float)
    @arduinoobjectmethod
    def getTempF(self, address_or_index):
        pass

    @classmethod
    def toCelsius(cls, value):
        return (value - 32) * 5/9

    @classmethod
    def toFahrenheit(cls, value):
        return (value * 9/5) + 32


