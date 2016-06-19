from flask import Blueprint, redirect, Response, request, session, make_response
from user.user import User
import json

def add_routes(app=None):
    userAuthentification = Blueprint('User', __name__, url_prefix='/user')

    @userAuthentification.route('/login', methods=['POST', ])
    def login():
        email = request.form['email']
        password = request.form['password']
        userHandle = User()
        responseId, session = userHandle.authenticate(email, password, request.environ['REMOTE_ADDR'])
        responseData ={
            'code':responseId,
        }
        responseData = json.dumps(responseData)
        print(responseData)
        response = make_response(responseData)
        if (responseId == 310):
            response.set_cookie('session', value=session)
            print(response)
            return response
        return response

    @userAuthentification.route('/logout',methods=['POST',])
    def logout():
        userHandle = User()
        session=request.cookies['session']
        userHandle.logout(session)
        data = json.dumps({'successful':True})
        response = make_response(data)
        response.set_cookie('session','',expires=0)
        return response

    app.register_blueprint(userAuthentification)


def get_info(session):
    userHandle = user.User()
    info = {}
    loggedIn = userHandle.is_logged_in(session)
    if (loggedIn):
        userInfo = userHandle.info_by_session(session)
        info['permission'] = userInfo['permission']
        info['email'] = userInfo['email']
        info['name'] = userInfo['name']
        info['logged'] = True
    else:
        info['logged'] = False
        info['permission'] = 20
    return info
