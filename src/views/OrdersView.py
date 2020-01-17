
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.OrdersModel import OrdersModel, OrderSchema

order_api = Blueprint('order_api', __name__)
orders_schema = OrderSchema()


@order_api.route('/', methods=['POST'])
@Auth.auth_required
def create():

    req_data = request.get_json()
    req_data['owner_id'] = g.user.get('id')
    data, error = orders_schema.load(req_data)
    if error:
        return custom_response(error, 400)
    order = OrdersModel(data)
    order.save()
    data = orders_schema.dump(order).data
    return custom_response(data, 201)


@order_api.route('/', methods=['GET'])
def get_all():

    orders = OrdersModel.get_all_sales()
    data = orders_schema.dump(orders, many=True).data
    return custom_response(data, 200)


@order_api.route('/<int:order_id>', methods=['GET'])
def get_one(blogpost_id):

    post = OrdersModel.get_one_blogpost(blogpost_id)
    if not post:
        return custom_response({'error': 'order not found'}, 404)
    data = orders_schema.dump(post).data
    return custom_response(data, 200)


@order_api.route('/<int:order_id>', methods=['DELETE'])
@Auth.auth_required
def delete(sale_id):
    """
  Delete
  """
    order = OrdersModel.get_one_sale(sale_id)
    if not order:
        return custom_response({'error': 'order not found'}, 404)
    data = orders_schema.dump(order).data
    if data.get('owner_id') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    order.delete()
    return custom_response({'message': 'deleted'}, 204)


def custom_response(res, status_code):
    """
  Custom Response Function
  """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )