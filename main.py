import jinja2
import psycopg2
from flask import Flask, render_template, request

from assets import get_page, generate_menu_links
from modules.User import get_info
from settings import settings

template_dir = ['templates','modules/']
loader = jinja2.FileSystemLoader(template_dir)


app = Flask(__name__)
app.debug = True
app.secret_key = 'cd217450d3b793b8b47671cf51ae2e98efb3b38f2d2b522a04b7046aad1ab165cc2834e7a4fa86d722fd5a8810b4e1d798222b109ffdb77beac5faca136d0287'
app.jinja_loader = loader
conn = psycopg2.connect("dbname='opeteth' user='postgres' host='localhost' password='N0PLZeFLEv'")


@app.route('/')
def auth():
    info = {}
    if 'session' in request.cookies:
        info = get_info(request.cookies['session'])
    else:
        info = {'logged': False, 'permission': 20,'scope':['guest']}
    return render_template('index.jinja2', menu=generate_menu_links(), info=info)


@app.route('/<string:page_name>')
def page(page_name):
    info = {}
    if 'session' in request.cookies:
        info = get_info(request.cookies['session'])
    else:
        info = {'logged': False, 'permission': 20}
    return render_template('index.jinja2', menu=generate_menu_links(), info=info)

@app.route('/<string:module_name>/<string:page_name>')
def modulePage(module_name,page_name):
   return page(page_name)

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
        info = {'logged': False, 'permission': 20,'scope':['guest']}

    return get_page(page_name,info['permission'],info['scope'])


for moduleInfo in settings['modules']:
    # try:
    module = __import__(settings['paths']['modules'] +'.' + moduleInfo['package-path'])
    module = getattr(module,moduleInfo['package-path'])
    module.add_blueprint(app)



#User.add_routes(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
