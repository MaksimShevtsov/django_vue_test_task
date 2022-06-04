from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from shipments_app.models import ShippingMethod
from shipments_app.serializers import ShippingMethodSerializer


class ShippingMethodRepository:

    @staticmethod
    def get_all() -> Response:
        shipping_methods = ShippingMethod.objects.all()
        shipping_methods_serializer = ShippingMethodSerializer(shipping_methods, many=True)
        return Response(shipping_methods_serializer.data)

    @staticmethod
    def create(request: object) -> Response:
        shipping_methods_data = JSONParser().parse(request)
        shipping_methods_serializer = ShippingMethodSerializer(data=shipping_methods_data)
        if shipping_methods_serializer.is_valid():
            shipping_methods_serializer.save()
            return Response("Added Successfully")
        return Response("Failed to Add")

    @staticmethod
    def update(request: object) -> Response:
        shipping_methods_data = JSONParser().parse(request)
        shipping_method = ShippingMethod.objects.get(shipping_method_id=shipping_methods_data['shipping_method_id'])
        shipping_methods_serializer = ShippingMethodSerializer(shipping_method, data=shipping_methods_data)
        if shipping_methods_serializer.is_valid():
            shipping_methods_serializer.save()
            return Response("Updated Successfully")
        return Response("Failed to Update")

    @staticmethod
    def delete(id: int) -> Response:
        shipping_method = ShippingMethod.objects.get(shipping_method_id=id)
        shipping_method.delete()
        return Response("Deleted Successfully")
