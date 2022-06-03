from django.views.decorators.csrf import csrf_exempt

from shipments_app.services.order_repository import OrdersRepository
from shipments_app.services.customer_repository import CustomerRepository
from shipments_app.services.shippingmethod_repository import ShippingMethodRepository


@csrf_exempt
def shipping_method_api(request, id=0):
    if request.method == 'GET':
        return ShippingMethodRepository.get_all()

    elif request.method == 'POST':
        return ShippingMethodRepository.create(request)

    elif request.method == 'PUT':
        return ShippingMethodRepository.update(request)

    elif request.method == 'DELETE':
        return ShippingMethodRepository.delete(id)


@csrf_exempt
def customer_api(request, id=0):
    if request.method == 'GET':
        return CustomerRepository.get_all()

    elif request.method == 'POST':
        return CustomerRepository.create(request)

    elif request.method == 'PUT':
        return CustomerRepository.update(request)

    elif request.method == 'DELETE':
        return CustomerRepository.delete(id)


@csrf_exempt
def order_api(request, id=0):
    if request.method == 'GET':
        return OrdersRepository.get_all()

    elif request.method == 'POST':
        return OrdersRepository.create(request)

    elif request.method == 'PUT':
        return OrdersRepository.update(request)

    elif request.method == 'DELETE':
        return OrdersRepository.delete(id)
