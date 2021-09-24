from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config_options


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong' #provides different security levels.
login_manager.login_view = 'auth.login' #if someone tries a page and  is not logged in then we should redirect them to ?

def create_app(config_name):
    # creating a flask application
    app = Flask(__name__)


    # creating the app configurations
    app.config.from_object(config_options[config_name])

    # initialize flask applications
    db.init_app(app)
    login_manager.init_app(app)
    from .views import views 
    from .auth import auth 

    app.register_blueprint(views,url_prefix = '/')
    app.register_blueprint(auth,url_prefix = '/')

    from .models import User,Post,Comment,Like
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

