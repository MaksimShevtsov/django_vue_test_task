from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from shipments_app.models import Order
from shipments_app.serializers import OrderSerializer, OrderPostSerializer


class OrdersRepository:

    @staticmethod
    def get_all() -> Response:
        data = Order.objects.select_related('customer', 'shipping_method')
        serializer = OrderSerializer(data, many=True)
        return Response(serializer.data)

    @staticmethod
    def create(request) -> Response:
        data = JSONParser().parse(request)
        data_serializer = OrderPostSerializer(data=data)
        if data_serializer.is_valid():
            data_serializer.save()
            return Response("Added Successfully")
        return Response("Failed to Add")

    @staticmethod
    def update(request) -> Response:
        data = JSONParser().parse(request)
        method = Order.objects.get(order_id=data['order_id'])
        order_methods_serializer = OrderPostSerializer(method, data=data)
        if order_methods_serializer.is_valid():
            order_methods_serializer.save()
            return Response("Updated Successfully")
        return Response("Failed to Update")

    @staticmethod
    def delete(id: int) -> Response:
        method = Order.objects.get(order_id=id)
        method.delete()
        return Response("Deleted Successfully")
