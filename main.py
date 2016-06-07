from flask import Flask, url_for, render_template,request
from settings import settings
from assets import get_page,generate_menu_links
import jinja2
import psycopg2
template_dir = 'templates'
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)

app = Flask(__name__)
app.debug = True

conn = psycopg2.connect("dbname='opeteth' user='postgres' host='localhost' password='N0PLZeFLEv'")

@app.route('/<string:page_name>')
def page(page_name):
    return render_template('index.jinja2', menu=generate_menu_links())

@app.route('/<string:page_name>/api/<string:request>')
def api(page_name,request):
    raise NotImplemented

@app.route('/')
def index():

    return render_template('index.jinja2',menu=generate_menu_links() )

@app.route('/pages/<string:page_name>')
def pages(page_name):
    return get_page(page_name)

if __name__ == '__main__':
    app.run(host="0.0.0.0")