import os



class Config(object):
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
            "postgres://", "postgresql://", 1)

    


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    

config_options = {
'development':DevConfig,
'production':ProdConfig
} 