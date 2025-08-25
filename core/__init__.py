'''
create the application instance
initialize the app with the configuration settings
'''
from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db  = SQLAlchemy()
bcrypt = Bcrypt()
limiter = Limiter(key_func=get_remote_address)

def create_app():
    '''
    creates the application instance and returns it
    '''
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    limiter.init_app(app)

    return app



