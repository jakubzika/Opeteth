from flask import Flask, url_for, render_template, request, sessions, Blueprint
from settings import settings
from assets import get_page, generate_menu_links
import jinja2
import psycopg2
from user import add_routes, get_info

template_dir = 'templates'
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)
import user

app = Flask(__name__)
app.debug = True
app.secret_key = 'cd217450d3b793b8b47671cf51ae2e98efb3b38f2d2b522a04b7046aad1ab165cc2834e7a4fa86d722fd5a8810b4e1d798222b109ffdb77beac5faca136d0287'

conn = psycopg2.connect("dbname='opeteth' user='postgres' host='localhost' password='N0PLZeFLEv'")


@app.route('/')
def auth():
    info = {}
    if 'session' in request.cookies:
        info = get_info(request.cookies['session'])
    else:
        info = {'logged': False, 'permission': 20}
    return render_template('index.jinja2', menu=generate_menu_links(), info=info)


@app.route('/<string:page_name>')
def page(page_name):
    info = {}
    if 'session' in request.cookies:
        info = get_info(request.cookies['session'])
    else:
        info = {'logged': False, 'permission': 20}
    return render_template('index.jinja2', menu=generate_menu_links(), info=info)


@app.route('/<string:page_name>/api/<string:request>')
def api(page_name, request):
    raise NotImplemented


@app.route('/')
def index():
    return render_template('index.jinja2', menu=generate_menu_links())


@app.route('/pages/<string:page_name>')
def pages(page_name):
    info = {}
    if 'session' in request.cookies:
        info = get_info(request.cookies['session'])
    else:
        info = {'logged': False, 'permission': 20}

    return get_page(page_name,info['permission'])


user.add_routes(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
