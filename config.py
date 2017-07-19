import os 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = ['Flasky']
    FLASK_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.kingorient.com'
    MAIL_PORT = 25
    MAIL_USE_TLS =False 
    MAIL_USERNAME = 'zabbix@kingorient.com'
    MAIL_PASSWORDD = 'Ha123456'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:happyboy@localhost/flask_study'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:happyboy@localhost/flask_study'

class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:happyboy@localhost/flask_study'

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'product':ProductConfig,
    'default':DevelopmentConfig,
    }

    
