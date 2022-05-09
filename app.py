import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .main import main as main_blueprint 


db=SQLAlchemy()

from .main import models

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wordpass'
    app.register_blueprint(main_blueprint)
    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')
   
    db.init_app(app)
    migrate = Migrate(app,db)
    
    return app


if __name__=='__main__':
    create_app()

