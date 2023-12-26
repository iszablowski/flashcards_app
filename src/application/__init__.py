from flask import Flask
from .auth import auth
from .user import user
from .cards import cards
from .home import home

def create_app():

    app = Flask(__name__)
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(home)
    app.register_blueprint(cards)

    return app

