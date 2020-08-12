import os
from datetime import datetime

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_SECRET = SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Dev(Config):
    DEBUG = True
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI_DEV')

class Prod(Config):
    DEBUG = False
    DEVELOPMENT = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI_PROD')
