from flask import Flask, url_for, render_template
from build import generatePage
# Opeteth project

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():

    user = {'name': 'Jakub', 'rights': 'none'}
    notes = {'count': {
        'day': 0,
        'week': 1,
        'month': 5,
    },
        'mentions': 8
    }
    generatePage()
    return render_template('template.jinja2')


@app.route('/isup')
def hello():
    return 'not implemented'


with app.test_request_context():
    url_for('static', filename='main.css')

if __name__ == '__main__':
    app.run()
