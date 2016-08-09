from flask import Blueprint, request, make_response



def test():
    print('Called ', __name__)

adminTools = Blueprint('AdminTools', __name__, url_prefix='/api/admin')

@adminTools.route('/foo')
def foo():
    return 'Foo Bar'

def add_blueprint(app=None):
    app.register_blueprint(adminTools)
