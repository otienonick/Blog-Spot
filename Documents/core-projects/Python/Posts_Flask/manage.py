
from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server
from app.models import User,Post


# creating app instance
app = create_app('development')


migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('server',Server)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app,db = db,User = User,Post = Post) 

if __name__ == '__main__':
    manager.run()

#   whenever you make a change to your python code it will automatically rerun the flask web server
