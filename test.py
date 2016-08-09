from settings import settings
import modules.User


for module in settings['modules']:
    package = settings['paths']['modules']+'.'+module['package-path']
    # print(package)
    a = __import__(settings['paths']['modules']+'.'+module['package-path'])
    b = getattr(a,module['package-path'])
    b.add_blueprint()
    # help(a)
