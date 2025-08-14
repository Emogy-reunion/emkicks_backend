from core import db, bcrypt
from sqlalchemy.dialects.postgresql import UUID, ENUM
import uuid
from datetime import datetime
from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func

class Users(db.Model):
    '''
    stores the user authentication details
    '''
    id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False, unique=True, default=uuid.uuid4)
    email = db.Column(db.String(50), nullable=False, unique=True)
    passwordhash = db.Column(db.String(100), nullable=False)
    role = db.Column(ENUM('member', 'admin', 'superadmin', name='role_enum'), nullable=False, default='member')
    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    registered_on = db.Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
