# src/models/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db
db = SQLAlchemy()
bcrypt = Bcrypt()

from .SalesModel import SalesModel, SaleSchema
from .OrdersModel import OrdersModel, OrderSchema
from .UserModel import UserModel, UserSchema
