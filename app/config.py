class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Drygoker1234#@localhost/nataliblog'
    SECRET_KEY = 'bueatifull smart screen'

  ####  Flask Security  #####
    SECURITY_PASSWORD_SALT = 'Salt and Pasw'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'