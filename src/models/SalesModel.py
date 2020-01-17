from . import db
import datetime
from marshmallow import fields, Schema

class SalesModel(db.Model):

    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    sale = db.Column(db.String(50), nullable=False)

    def __init__(self, data):
        self.order_id = data.get('order_id')
        self.sales = data.get('sale')


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_sales():
        return SalesModel.query.all()

    @staticmethod
    def get_one_sale(id):
        return SalesModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)

class SaleSchema(Schema):
    id = fields.Int(dump_only=True)
    order_id = fields.Int(required=True)
    sales = fields.Str(required=True)