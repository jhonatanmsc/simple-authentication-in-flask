import os.path

from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = config('DEBUG', default=False)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, config("DB"))
SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATIONS", default=False)
SECRET_KEY = config("SECRET_KEY")