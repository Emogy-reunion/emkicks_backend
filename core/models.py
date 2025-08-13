from core import db, bcrypt
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Users(db.Model):
    '''
    stores the user authentication details
    '''
    id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False, unique=True, default=uuid.uuid4)
