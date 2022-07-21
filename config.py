import os
import re


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Drygoker1234#@localhost/nataliblog'
    uri = os.getenv("DATABASE_URL") 
    if uri.startswith("postgres://"):
      uri = uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = uri
    SECRET_KEY = 'bueatifull smart screen'


  ####  Flask Security  #####
    SECURITY_PASSWORD_SALT = 'Salt and Pasw'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'