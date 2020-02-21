#src/app.py

from flask import Flask, render_template, redirect, url_for

from .config import app_config
from .models import db, bcrypt
from .views.UserView import user_api as user_blueprint
from .views.SalesView import sales_api as sale_blueprint
from .views.OrdersView import order_api as order_blueprint

def create_app(env_name):

    # app initiliazation
    app = Flask(__name__)
    #app.config.from_object(app_config[env_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://User01:777@localhost/food_delivery'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # initializing bcrypt
    bcrypt.init_app(app)  # add this linese

    db.init_app(app)  # add this line


    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users') # add this line
    app.register_blueprint(sale_blueprint, url_prefix='/api/v1/sales')
    app.register_blueprint(order_blueprint, url_prefix='/api/v1/orders')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return "HELLO WORLD"



    return app
