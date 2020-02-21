# /src/config.py

import os

class Development(object):

    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') #or 'hhgaghhgsdhdhdd'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') #or 'postgresql://User01:777@localhost/food_delivery'
class Production(object):

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')# or 'postgresql://User01:777@localhost/food_delivery'
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')# or 'hhgaghhgsdhdhdd'

class Testing(object):

    TESTING = True
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') # or 'hhgaghhgsdhdhdd'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')# or 'postgresql://User01:777@localhost/food_delivery'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}

