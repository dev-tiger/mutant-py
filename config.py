"""[General Configuration Params]
"""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:

    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    APP_HOST = environ.get("APP_HOST")
    APP_PORT = environ.get("HOST_PORT")
    DB_NAME = environ.get("DB_NAME")
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    POKEMONS_TABLE = environ.get("POKEMONS_TABLE")
    POKEMONS_CSV_PATH = environ.get("POKEMONS_CSV_PATH")
    SECRET_KEY = environ.get("SECRET_KEY")
    TOKEN_EXPIRATION = environ.get("TOKEN_EXPIRATION")
    PIPENV_DONT_LOAD_ENV = environ.get("PIPENV_DONT_LOAD_ENV")
