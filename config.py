

class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Drygoker1234#@localhost/nataliblog'
    SQLALCHEMY_DATABASE_URI = 'postgres://hhfbrywyqgfbtj:2e6ed6ba62f031812521171f9f26d9595ac7b2dfbd39446963ccf6b0704e3a1d@ec2-54-211-255-161.compute-1.amazonaws.com:5432/d4m35ar4vln358'
    SECRET_KEY = 'bueatifull smart screen'


  ####  Flask Security  #####
    SECURITY_PASSWORD_SALT = 'Salt and Pasw'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'