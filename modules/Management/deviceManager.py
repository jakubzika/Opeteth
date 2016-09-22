from modules.Management.ping import ping
from lib.utils import loadComputersInfo,getComputerList, convertDictToJson
import json

class DeviceManager:

    def __init__(self):
        self.computerInfo = loadComputersInfo()

    def pingDevices(self):
        deviceState = {}
        deviceList = getComputerList()
        for index, device in enumerate(self.computerInfo['computers']):
            if(ping(device['IP-address']) != None):
                deviceList[index]['state'] = 'running'
            else:
                deviceList[index]['state'] = 'unreachable'
        return deviceList

    def saveActivityToFile(self):
        deviceList = self.pingDevices()
        deviceListJSON = convertDictToJson(deviceList)
        file = open('temp/activity.json','w')
        file.write(deviceListJSON)


if __name__ == '__main__':
    pass