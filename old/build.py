from flask import url_for, render_template

from old.settings import settings, userState


def generatePage():
    dependenciesHead, dependenciesBody = build_dependencies()
    menu = build_menu()

    content = {

    }


def build_dependencies():
    pathsHead = makePath(settings['dependencies']['head'])
    dependenciesHead = render_template('templates/dependencies-head.jinja2', dependencies=pathsHead)
    pathsBody = makePath(settings['dependencies']['body'])
    dependenciesBody = render_template('templates/dependencies-body.jinja2', dependencies=pathsBody)
    return dependenciesHead, dependenciesBody


def makePath(dependencies):
    paths = []
    path = {}
    for index, i in enumerate(dependencies):

        if i.split('.')[-1] == 'css':
            path = {
                'rel': 'stylesheet',
                'type': 'text/css',
                'path': url_for('static', filename=i),
            }
        elif i.split('.')[-1] == 'js':
            path = {
                'path': url_for('static', filename=i),
            }
        paths.append(path)

    return paths


def build_sidebar():
    menu=build_menu()
    modules=build_modules()


def build_menu():
    menuContents = []

    for index, i in enumerate(settings['menu']):
        if userState <= settings['menu'][index]['visibility']:
            menuContents.append(i)

    menu = render_template('templates/menu.jinja2', menu=menuContents)
    return menu

def build_modules():
    pass