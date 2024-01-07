import os
from decouple import config
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Config:
    SECRET_KEY = config('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')

    # JWT_VERIFY_EXPIRATION = True
    # JWT_LONG_RUNNING_REFRESH_TOKEN = True
    # JWT_EXPIRATION_DELTA = timedelta(minutes=600),  # For "Access Token"
    # JWT_REFRESH_EXPIRATION_DELTA = timedelta(days=7),  # For "Refresh Token"


class DevConfig(Config):
    SQLALCHEMY_BINDS = {
        'WebApps': 'Removed',
        'WebAppsTender': 'Removed',
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    DEBUG = True


# class TestConfig(Config):
#     TESTING=True
#     SQLALCHEMY_DATABASE_URI="sqlite://"
#     SQLALCHEMY_TRACK_MODIFICATIONS=False
#     SQLALCHEMY_ECHO=True


# class ProdConfig(Config):
#     SQLALCHEMY_DATABASE_URI=uri
#     SQLALCHEMY_TRACK_MODIFICATIONS=False
#     DEBUG=config('DEBUG',cast=bool)


config_dict = {
    'dev': DevConfig,
    # 'testing': TestConfig,
    # 'production': ProdConfig
}