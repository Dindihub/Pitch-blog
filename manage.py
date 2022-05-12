from app import create_app,db
from flask_script import Manager,Server
from app.main.models import User,Pitch,Category,Votes,Comments
from flask_migrate import Migrate,MigrateCommand

#create an instance of app


app = create_app('development')
# app = create_app('test')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User 
    ,Pitches=Pitch,Category=Category,Votes=Votes,Comments=Comments)




if __name__=='__main__':
    manager.run()
