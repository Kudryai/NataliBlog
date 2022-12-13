import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
    DEBUG = os.getenv("DEBUG")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
    }

    ### Cookie ###

    REMEMBER_COOKIE_SAMESITE = "strict"
    SESSION_COOKIE_SAMESITE = "strict"

    ####  Flask Security  #####

    SECURITY_PASSWORD_SALT = "Salt and Pasw"
    SECURITY_PASSWORD_HASH = os.getenv("SECURITY_PASSWORD_HASH")
    SECURITY_REGISTERABLE = True
    SECURITY_USERNAME_ENABLE = True
    SECURITY_SEND_REGISTER_EMAIL = True
    SECURITY_UNAUTHORIZED_VIEW = "/blog/"
    SECURITY_MSG_LOGIN = ("Надо зарегестрироваться", "info")
    SECURITY_RECOVERABLE = True
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = 25
    MAIL_USE_TSL = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")
