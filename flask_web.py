from flask import Flask, url_for, render_template

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
    return render_template('main.jinja2', user=user, notes=notes)


@app.route('/isup')
def hello():
    return 'not implemented'


with app.test_request_context():
    url_for('static', filename='main.css')

if __name__ == '__main__':
    app.run()
