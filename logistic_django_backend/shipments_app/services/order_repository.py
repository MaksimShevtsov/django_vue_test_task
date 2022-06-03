from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from shipments_app.models import Order
from shipments_app.serializers import OrderSerializer, OrderPostSerializer


class OrdersRepository:

    @staticmethod
    def get_all() -> JsonResponse:
        data = Order.objects.select_related('customer', 'shipping_method')
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
        method = Order.objects.get(order_id=data['order_id'])
        order_methods_serializer = OrderPostSerializer(method, data=data)
        if order_methods_serializer.is_valid():
            order_methods_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    @staticmethod
    def delete(id: int) -> JsonResponse:
        method = Order.objects.get(order_id=id)
        method.delete()
        return JsonResponse("Deleted Successfully", safe=False)
