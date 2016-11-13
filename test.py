from settings import settings
import modules.User
from modules.Management.deviceManager import DeviceManager
from lib.taskScheduler import spawnThread
from lib.utils import getDatabaseInfo

def foo():
    for module in settings['modules']:
        package = settings['paths']['modules']+'.'+module['package-path']
        # print(package)
        a = __import__(settings['paths']['modules']+'.'+module['package-path'])
        b = getattr(a,module['package-path'])
        b.add_blueprint()
        # help(a)

def test(a):
    a=5


if __name__ == '__main__':
    print(getDatabaseInfo())
    #device = DeviceManager()
    #evice.pingDevices()
    #device.saveActivityToFile()