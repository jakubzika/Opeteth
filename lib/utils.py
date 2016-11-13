from settings import settings
import yaml
import json

def getUserScope():
    raise NotImplemented


def convertSettingsScopeToArray():
    scopeArray = []
    for i in settings['scopes']:
        scopeArray.append(i['name'])
    return scopeArray


def convertStringScopeToArray(scopeString):
    return scopeString.split(',')


def loadComputersInfo():
    file = open('data/computers.yml','r')
    deviceInfo = yaml.load(file.read())
    file.close()
    return deviceInfo

def getComputerList():
    computers = loadComputersInfo()
    cleanedComputersList = []
    for index,b in enumerate(computers['computers']):
        temp = {}
        temp['name'] = b['name']
        temp['WOL'] = b['WOL']
        temp['id'] = index
        cleanedComputersList.append(temp)
    return cleanedComputersList

def convertDictToJson(value):
    return json.dumps(value)

def getDeviceActivity():
    pass

def getDatabaseInfo():
    file = open('secret.yaml','r')
    dataRaw = file.read()
    data = yaml.load(dataRaw)
    return data['database']

def getDatabaseConnectString():
    info = getDatabaseInfo()
    string = """dbname='{dbname}' user='{user}' host='{host}' password='{password}'""".format(dbname=info['database-name'],user=info['username'],host=info['host'],password=info['password'])
    return string

if __name__ == '__main__':
    pass
