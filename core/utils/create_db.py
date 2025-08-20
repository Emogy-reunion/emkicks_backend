'''
creates the tables
'''
from core import db
from core.models import Users, Profiles


def create_tables():
    db.create_all()
