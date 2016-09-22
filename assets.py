from flask import render_template
from settings import settings

def get_page(pageName,permission,scope):
    for i in settings['pages']:
        if(pageName == i['uri']):
            print(i['scope'])
            print(scope)
            for a in scope:
                if(a in i['scope']):
                    return render_template(settings['paths']['pages']+i['path']+'.jinja2')
                else:
                    return render_template(settings['paths']['pages']+'permission.jinja2')
    return '404 not found'

def get_info():
    raise NotImplemented

def generate_menu_links():
    data=[]
    temp={}
    for i in settings['menu']:
        temp={}
        temp['name']=i['name']
        temp['url']='not found'
        temp['permission'] = i['permission']
        for j in settings['pages']:
            if j['name']== i['link-to']:
                temp['url']=j['path']

        data.append(temp)
    return data


def importModules(app):
    raise NotImplemented