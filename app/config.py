import os



class Config(object):
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    

config_options = {
'development':DevConfig,
'production':ProdConfig
} 