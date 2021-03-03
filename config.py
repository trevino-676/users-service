"""
author: Luis Manuel Torres Trevino
description: This file contains all app configurations
"""
from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
DOTENV_PATH = path.join(BASE_DIR, ".env")
load_dotenv(DOTENV_PATH)

class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    DEBUG = environ.get("FLASK_DEBUG")

    # Database Config
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
