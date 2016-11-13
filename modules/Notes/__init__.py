from flask import Blueprint, request, make_response
from modules.User import get_info
import jinja2
import json
from time import time

notesPath = './data/notes.json'
template_dir = 'modules/Notes/templates'

loader = jinja2.FileSystemLoader(template_dir)


def add_blueprint(app=None):
    notesApi = Blueprint('NotesAPI', __name__, url_prefix='/api/notes')
    notes = Blueprint('Notes', __name__, url_prefix='/notes')
    notes.jinja_loader = loader
    print('registered Notes')

    @notesApi.route('/', methods=['GET'])
    def getNotes():
        data = json.loads(request.args.get('data'))
        print(data)
        if (data['filter'] == None or data['filter'] == -1):
            file = open('./data/notes.json', 'r')
            data = file.read()
            file.close()
            return data
        else:
            pass

    @notesApi.route('/groups/',methods=['GET'])
    def knownFilters():
        file = open(notesPath, 'r')
        data = file.read()
        data = json.loads(data)
        groups = data['groups']
        return json.dumps(groups)

    @notesApi.route('/', methods=['POST'])
    def createNote():
        data = json.loads(request.form['data'])
        file = open(notesPath, 'r')
        notesData = file.read()
        file.close()
        notesData = json.loads(notesData)
        # newNote = {notesData['id']:data['note']}
        data['note']['submitted'] =
        notesData['notes'][notesData['id']] = data['note']
        notesData['id'] += 1
        file = open(notesPath, 'w')
        file.write(json.dumps(notesData))
        file.close()
        return json.dumps({
            'status': 'successful'
        })

    @app.route('/api/notes/<int:note_id>', methods=['PUT'])
    def editNote(note_id):
        data = json.loads(request.form['data'])

    app.register_blueprint(notes)
    app.register_blueprint(notesApi)
