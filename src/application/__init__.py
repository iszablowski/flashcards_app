from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from os import getenv

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

    db.init_app(app)

    from .auth import auth
    app.register_blueprint(auth)

    from .user import user
    app.register_blueprint(user)

    from .home import home
    app.register_blueprint(home)

    from .cards import cards
    app.register_blueprint(cards)

    from .models.user_model import User
    from .models.collection_model import FlashcardsCollection
    from .models.flashcard_model import Flashcard

    with app.app_context():
        db.create_all()

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

