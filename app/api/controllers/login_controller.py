"""
"""
from app.models.users import User
from app.api.controllers.encrypt_password import check_password


def authenticate(username, password):
    user = User.query.filter_by(username = username).first()
    if user and check_password(password, user.password) and user.active:
        return user


def identity(payload):
    id = payload['identity']
    return User.query.filter_by(id = id).first()