from flask import render_template, request
import settings
from modules.User import get_info
from importlib import import_module

def register_pages(moduleName,page_name):
    moduleSettings = {}
    # try:
    moduleSettings = import_module('modules.{0}.settings'.format(moduleName))
    moduleSettings = moduleSettings.settings
    # except Exception as e:
    #     print(e)
    #     print('Could not find module settings')
    #     return None
    info = {}
    if 'session' in request.cookies:
        info = get_info(request.cookies['session'])
    else:
        info = {'logged': False, 'permission': 20, 'scope': ['guest']}
    for i in moduleSettings['pages']:
        if(page_name == i['name']):
            print(info['scope'],i['scope'])
            print(info['scope'] in i['scope'])
            for a in info['scope']:
                if(a in i['scope']):
                    return render_template(i['path']+'.jinja2')
    return '404 not found'