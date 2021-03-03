"""
author: Luis Manuel Torres Trevino
description: This file contains the data access methods
    for user model
"""
from app.models.users import User
from app import db
from app.api.controllers.encrypt_password import encrypt_password


class UserController:

    def get_users(self, limit, offset, deleted_users=True):
        """ Returns all users in the database

            Parameters
            ----------
                limit: <int> limit of users.
                offset: <int> initial user.
                deleted_user: <bool> returns the deleted users.
        """
        users = User.query.filter_by(active = deleted_users).all()
        return users

    
    def new_user(self, username, mail, first_name, last_name, password, company, admin=False):
        """ Create a new instance of User and save to database

            Parameters
            ----------
                username: Username of User.
                mail: user email.
                first_name: user first_name.
                last_name: user last_name.
                password: user password
                admin: flag for user admin.
        """
        try:
            hash_pass = encrypt_password(password)
            user = User(username, mail, first_name, last_name, hash_pass, company, admin)
            db.session.add(user)
            db.session.commit()
            return True
        except Exception as e:
            print(f"failed add user {user}")
            print(e)
            return False

    def update_user(self, old_id, username=None, mail=None, first_name=None,
                    last_name=None, password=None, admin=False):
        """ Update user information
        """
        try:
            user = User.query.filter_by(id = old_id).first()
            user.username = username if username is not None else user.username
            user.mail = mail if mail is not None else user.mail
            user.first_name = first_name if first_name is not None else user.first_name
            user.last_name = last_name if last_name is not None else user.last_name
            user.password = encrypt_password(password) \
                if password is not None else user.password
            user.admin = admin if admin is not None else user.admin
            db.session.commit()
            return True
        except Exception as e:
            print(f"Failed update user {user}")
            print(e)
            return False

    def delete_user(self, user_id):
        """ Delete the user
        """
        try:
            user = User.query.filter_by(id = user_id).first()
            user.active = False
            db.session.commit()
            return True
        except Exception as e:
            print(f"Failed deleted user {user}")
            print(e)
            return False