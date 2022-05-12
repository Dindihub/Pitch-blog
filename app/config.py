import os



class Config(object):
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # SQLALCHEMY_DATABASE_URI='postgres://bnpegjulzxkznr:754192c1cc4cc0ddc69dcfef3800b75f6b550ec9b87821acee76c0cfd2b511dc@ec2-52-4-104-184.compute-1.amazonaws.com:5432/d966counsre75h'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://bnpegjulzxkznr:754192c1cc4cc0ddc69dcfef3800b75f6b550ec9b87821acee76c0cfd2b511dc@ec2-52-4-104-184.compute-1.amazonaws.com:5432/d966counsre75h'
    DEBUG =True


class DevConfig(Config):
    DEBUG = True
    

config_options = {
'development':DevConfig,
'production':ProdConfig
} 