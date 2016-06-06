from flask import Flask, url_for, render_template
from settings import settings
from assets import get_page
import jinja2

template_dir = 'templates'
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.jinja2', )

@app.route('/pages/<string:page_name>')
def pages(page_name):
    return get_page(page_name)

if __name__ == '__main__':
    app.run()