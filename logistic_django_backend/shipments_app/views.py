from rest_framework.decorators import api_view

from shipments_app.services.order_repository import OrdersRepository
from shipments_app.services.customer_repository import CustomerRepository
from shipments_app.services.shippingmethod_repository import ShippingMethodRepository


@api_view(['GET', 'POST', 'PUT'])
def shipping_method_api(request):
    if request.method == 'GET':
        return ShippingMethodRepository.get_all()

    elif request.method == 'POST':
        return ShippingMethodRepository.create(request)

    elif request.method == 'PUT':
        return ShippingMethodRepository.update(request)


@api_view(['DELETE'])
def shipping_method_api_delete(request, id=0):
    return ShippingMethodRepository.delete(id)


@api_view(['GET', 'POST', 'PUT'])
def customer_api(request, id=0):
    if request.method == 'GET':
        return CustomerRepository.get_all()

    elif request.method == 'POST':
        return CustomerRepository.create(request)

    elif request.method == 'PUT':
        return CustomerRepository.update(request)


@api_view(['DELETE'])
def customer_api_delete(request, id=0):
    return CustomerRepository.delete(id)


@api_view(['GET', 'POST', 'PUT'])
def order_api(request, id=0):
    if request.method == 'GET':
        return OrdersRepository.get_all()

    elif request.method == 'POST':
        return OrdersRepository.create(request)

    elif request.method == 'PUT':
        return OrdersRepository.update(request)


@api_view(['DELETE'])
def order_api_delete(request, id=0):
    return OrdersRepository.delete(id)
