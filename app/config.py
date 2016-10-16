import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['BLAKI_STOCK_SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['BLAKI_STOCK_DB_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True