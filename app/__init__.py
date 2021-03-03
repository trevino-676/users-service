"""
author: Luis Manuel Torres Trevino
description: This file contains the init_app function for the
    microservice.
"""
import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

from app.api.controllers.login_controller import authenticate, identity
jwt = JWT(app, authenticate, identity)

from app.api.routes import mod_user as user_module
from app.api.routes import company_routes

app.register_blueprint(user_module)
app.register_blueprint(company_routes)

db.create_all()