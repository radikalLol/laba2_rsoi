
from . import db
import datetime
from marshmallow import fields, Schema


class OrdersModel(db.Model):

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable = False)
    adress = db.Column(db.String(128), nullable=False)
    order = db.Column(db.Text, nullable=False)
    comment = db.Column(db.Text, nullable = False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ordered_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.name = data.get('name')
        self.adress = data.get('adress')
        self.order = data.get('order')
        self.comment = data.get('comment')
        self.owner_id = data.get('owner_id')
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
    order = fields.Str(required=True)
    comment = fields.Str(required=True)
    owner_id = fields.Int(required=True)
    ordered_at = fields.DateTime(dump_only=True)
