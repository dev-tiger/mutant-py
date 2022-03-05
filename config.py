"""[General Configuration Params]
"""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    APP_HOST = environ.get("APP_HOST")
    APP_PORT = environ.get("HOST_PORT")
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    SECRET_KEY = environ.get("SECRET_KEY")
    PIPENV_DONT_LOAD_ENV = environ.get("PIPENV_DONT_LOAD_ENV")


class ConfigTest:
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Mutant.2022@mutantdb-test.c1nt4f2g9lht.us-east-1.rds.amazonaws.com:5432/mutantdb'
    APP_HOST = environ.get("APP_HOST")
    APP_PORT = environ.get("HOST_PORT")
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    SECRET_KEY = environ.get("SECRET_KEY")
    PIPENV_DONT_LOAD_ENV = environ.get("PIPENV_DONT_LOAD_ENV")
    TESTING = True
    WTF_CSRF_ENABLED = False
