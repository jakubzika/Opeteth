from flask import Blueprint, request, make_response
from modules.User import get_info
import jinja2

template_dir = 'modules/Notes/templates'

loader = jinja2.FileSystemLoader(template_dir)


def add_blueprint(app=None):
    notesApi = Blueprint('NotesAPI', __name__, url_prefix='/api/notes')
    notes = Blueprint('Notes', __name__, url_prefix='/notes')
    notes.jinja_loader = loader
    app.register_blueprint(notes)
    app.register_blueprint(notesApi)
