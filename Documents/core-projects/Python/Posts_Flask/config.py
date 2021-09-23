import os
class Config:

    '''
    General configuration parent class
    
    '''


    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/posts'


class ProdConfig(Config):

    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class TestConfig(Config):
    pass



class DevConfig(Config):
    
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True



config_options = {

    'development':DevConfig,
    'production':ProdConfig,
}    

