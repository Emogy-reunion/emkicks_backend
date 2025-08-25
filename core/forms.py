'''
validates the applications form data
'''
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Email, Length, DataRequired, Regexp, EqualTo
from core.utils.custom_validators import no_emoji


class RegistrationForm(FlaskForm):
    '''
    validates the registration form data
    '''
    email = StringField('Email', validators=[
        DataRequired(message='Email is required'),
        Email(message='Please enter a valid email address'),
        Length(min=6, max=254, message='Email must be between 6 and 254 characters'),
        no_emoji
        ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message="Password must be at least 8 characters long!"),
        Regexp(r'(?=.*[A-Z])', message="Password must contain at least one uppercase letter!"),
        Regexp(r'(?=.*[a-z])', message="Password must contain at least one lowercase letter!"),
        Regexp(r'(?=.*\W)', message="Password must contain at least one special character!"),
        no_emoji
        ])
    confirmpassword = PasswordField('Confirm password', validators=[
        DataRequired(),
        EqualTo('password', message('Passwords must match')),
        ])
