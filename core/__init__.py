'''
create the application instance
initialize the app with the configuration settings
'''
from flask import Flask
from .config import Config

def create_app():
    '''
    creates the application instance and returns it
    '''
    app = Flask(__name__)
    app.config.from_object(Config)

    return app



