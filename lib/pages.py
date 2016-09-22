from flask import render_template, request
import settings
from modules.User import get_info

def register_pages(app, moduleName):
    try:
        moduleSettings = __import__('modules.{0}.settings'.format(moduleName))
        moduleSettings = moduleSettings.settings
    except Exception as e:
        print('Could not find module settings')
        return None
    @app.route('<string:page_name>',['GET',])
    def pages(page_name):
        print('route')
        info = {}
        if 'session' in request.cookies:
            info = get_info(request.cookies['session'])
        else:
            info = {'logged': False, 'permission': 20, 'scope': ['guest']}
        for i in moduleSettings['pages']:
            if(page_name == i['name']):
                if(info['scope'] in i['scope']):
                    return render_template(i['path']+'.jinja2')

    return app