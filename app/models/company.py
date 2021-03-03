"""
author: Luis Manuel Torres Trevino
description: This file contains the company model declaration
"""
from app import db


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp())
    users = db.relationship("User")
    
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return f"<Company {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
