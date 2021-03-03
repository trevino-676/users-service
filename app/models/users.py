"""
author: Luis Manuel Torres Trevino
description: This file contains the user model definition
"""
from app import db

class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=False, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.Text, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp())

    def __init__(self, username, email, first_name, last_name, password, company, admin):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.company_id = company
        self.admin = admin

    def __repr__(self):
        return f"<User {self.username}>"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }
