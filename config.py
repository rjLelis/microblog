import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KET', 'b929097fe346d0ae587b513e2c9a47a6313cc55a4f8b8f62')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASEDIR, 'app.db')
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False