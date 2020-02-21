# /src/config.py

import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or 'hhgaghhgsdhdhdd'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://User01:777@localhost/food_delivery'
class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://User01:777@localhost/food_delivery'
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or 'hhgaghhgsdhdhdd'

app_config = {
    'development': Development,
    'production': Production,
}

