'''
stores the applications configuration settings
'''
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URI')
