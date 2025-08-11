'''
create the application instance
'''
from flask import Flask

def create_app():
    '''
    creates the application instance and returns it
    '''
    app = Flask(__name__)
    return app



