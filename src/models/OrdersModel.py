
from . import db
import datetime
from marshmallow import fields, Schema


class OrdersModel(db.Model):

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable = False)
    adress = db.Column(db.String(128), nullable=False)
    orders = db.Column(db.Text, nullable=False)
    comments = db.Column(db.Text, nullable = False)
    order_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ordered_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.name = data.get('name')
        self.adress = data.get('adress')
        self.orders = data.get('order')
        self.comments = data.get('comment')
        self.order_id = data.get('order_id')
        self.ordered_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_orders():
        return OrdersModel.query.all()

    @staticmethod
    def get_one_order(id):
        return OrdersModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class OrderSchema(Schema):

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    adress = fields.Str(required=True)
    orders = fields.Str(required=True)
    comments = fields.Str(required=True)
    order_id = fields.Int(required=True)
    ordered_at = fields.DateTime(dump_only=True)