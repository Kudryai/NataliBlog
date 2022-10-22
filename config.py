import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Drygoker1234#@localhost/nataliblog'
    # os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://') or 
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Drygoker12345#@localhost/nataliblog' #os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://') or 'mysql+mysqlconnector://root:Drygoker1234#@localhost/nataliblog'
    SECRET_KEY = 'Best in the best'


  ####  Flask Security  #####
    SECURITY_PASSWORD_SALT = 'Salt and Pasw'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'