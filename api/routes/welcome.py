from flask import Blueprint

from api.controllers.welcome import WelcomeController

welcome = Blueprint('welcome_bp', __name__)


@welcome.route('/', methods=['GET'])
def index():
    return WelcomeController.index()
