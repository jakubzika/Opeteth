from flask import Blueprint, request, make_response, render_template
from modules.User import get_info
import jinja2
import  yaml
from lib.utils import convertDictToJson, getComputerList
from lib.taskScheduler import spawnThread
from modules.Management.deviceManager import DeviceManager
from lib.pages import register_pages

template_dir = 'modules/Management/templates'
loader = jinja2.FileSystemLoader(template_dir)

def add_blueprint(app=None):
    managementApi = Blueprint('ManagementAPI', __name__, url_prefix='/api/manage')
    management = Blueprint('management', __name__, url_prefix='/pages/manage')
    management.jinja_loader = loader

    # @management.route('/devices')
    # def devices():
    #     return render_template('devices.jinja2')

    @managementApi.route('/device-list',methods=['GET',])
    def deviceList():
        return convertDictToJson(getComputerList())

    @managementApi.route('/device-activity', methods=['GET', ])
    def deviceActivity():
        file = open('temp/activity.json','r')
        data = file.read()
        file.close()
        return data

    @managementApi.route('/device/<int:id>')
    def device(id):
        raise NotImplemented

    @management.route('/<string:page_name>')
    def page(page_name):
        return register_pages('Management',page_name)


    device = DeviceManager()
    spawnThread(5,device.saveActivityToFile)

    app.register_blueprint(management)
    app.register_blueprint(managementApi)