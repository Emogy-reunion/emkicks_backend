from core import db, bcrypt
import uuid
from datetime import datetime
from sqlalchemy import TIMESTAMP, Enum
from sqlalchemy.sql import func

class Users(db.Model):
    '''
    stores the user authentication details
    '''
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, nullable=False, unique=True, default=uuid.uuid4)
    email = db.Column(db.String(50), nullable=False, unique=True)
    passwordhash = db.Column(db.String(100), nullable=False)
    role = db.Column(Enum('member', 'admin', 'superadmin', name='role_enum'), nullable=False, default='member')
    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    registered_on = db.Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    profile = db.relationship('Profiles', back_populates='user', uselist=False, cascade='all, delete')

    def __init__(self, email, password):
        '''
        Instantiates the users model objects
        '''
        self.email = email
        self.passwordhash = self.generate_passwordhash(password)

    def generate_passwordhash(self, password):
        '''
        hashes the password to boost security
        '''
        return bcrypt.generate_password_hash(password)

    def check_passwordhash(self, password):
        '''
        compares the entered password with the stored hash
        '''
        return check_password_hash(self.passwordhash, password)



class Profiles(db.Model):
    '''
    stores the user profile information
    '''
    user_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('users.id', ondelete='cascade'), nullable=False, unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(Enum('male', 'female', 'other', name='gender_enum'))
    phone_number = db.Column(db.String(20))
    preffered_sizes = db.Column(db.ARRAY(db.String))
    shipping_address = db.Column(db.JSON)
    user = db.relationship('Users', back_populates='profile')

    def __init__(self, first_name, last_name, gender, phone_number, preffered_sizes, shipping_address):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone_number = phone_number
        self.preffered_sizes = preffered_sizes
        self.shipping_address = shipping_address
