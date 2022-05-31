from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ShipmentsApp.models import Order
from ShipmentsApp.serializers import OrderSerializer, OrderPostSerializer


class OrdersRepository(object):

    @staticmethod
    def get_all() -> JsonResponse:
        data = Order.objects.select_related('Customer', 'ShippingMethod')
        serializer = OrderSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    @staticmethod
    def create(request) -> JsonResponse:
        data = JSONParser().parse(request)
        data_serializer = OrderPostSerializer(data=data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    @staticmethod
    def update(request) -> JsonResponse:
        data = JSONParser().parse(request)
        method = Order.objects.get(OrderId=data['OrderId'])
        order_methods_serializer = OrderSerializer(method, data=data)
        if order_methods_serializer.is_valid():
            order_methods_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    @staticmethod
    def delete(id: int) -> JsonResponse:
        method = Order.objects.get(OrderId=id)
        method.delete()
        return JsonResponse("Deleted Successfully", safe=False)
