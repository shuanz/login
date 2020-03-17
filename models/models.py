from flask_user import UserMixin
from .. import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    is_enabled = db.Column(db.Boolean(), nullable=False, default=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, default='')

    # Extra data-model fields
    first_name = db.Column(db.String(50), nullable=False, default='')
    last_name  = db.Column(db.String(50), nullable=False, default='')

    # Define the relationship to Role via UserRoles
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))

# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    roles = db.relationship('User', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))
