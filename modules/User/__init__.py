import json

from flask import Blueprint, request, make_response
from modules.User.user import User


def add_blueprint(app=None):
    userAuthentification = Blueprint('User', __name__, url_prefix='/api/user')

    @userAuthentification.route('/login', methods=['POST', ])
    def login():
        email = request.form['email']
        password = request.form['password']
        userHandle = User()
        responseId, session = userHandle.authenticate(email, password, request.environ['REMOTE_ADDR'])
        responseData ={
            'code':responseId,
            'session':session,
        }
        responseData = json.dumps(responseData)
        print(responseData)
        response = make_response(responseData)
        if (responseId == 310):
            print('session',session)
            response.set_cookie('session', value=session)
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

    @userAuthentification.route('/info')
    def info():
        info = {}
        try:
            session= request.cookies['session']
            info = get_info(session)
        except Exception as e:
            info = get_info()

        return json.dumps(info)

    app.register_blueprint(userAuthentification)


def get_info(session = None):
    userHandle = user.User()
    info = {}
    if(session == None):
        info['logged'] = False
        info['permission'] = 20
        return info
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

def test():
    print('Called ',__name__)