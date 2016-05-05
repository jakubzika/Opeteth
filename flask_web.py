from flask import Flask, url_for, render_template

# Opeteth project

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.jinja2',)


@app.route('/isup')
def hello():
    return 'not implemented'

with app.test_request_context():
    url_for('static', filename='main.css')

if __name__ == '__main__':
    app.run()
