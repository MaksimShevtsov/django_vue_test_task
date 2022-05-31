from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ShipmentsApp.models import ShippingMethod
from ShipmentsApp.serializers import ShippingMethodSerializer


class ShippingMethodRepository(object):

    @staticmethod
    def get_all() -> JsonResponse:
        shipping_methods = ShippingMethod.objects.all()
        shipping_methods_serializer = ShippingMethodSerializer(shipping_methods, many=True)
        return JsonResponse(shipping_methods_serializer.data, safe=False)

    @staticmethod
    def create(request: object) -> JsonResponse:
        shipping_methods_data = JSONParser().parse(request)
        shipping_methods_serializer = ShippingMethodSerializer(data=shipping_methods_data)
        if shipping_methods_serializer.is_valid():
            shipping_methods_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    @staticmethod
    def update(request: object) -> JsonResponse:
        shipping_methods_data = JSONParser().parse(request)
        shipping_method = ShippingMethod.objects.get(ShippingMethodId=shipping_methods_data['ShippingMethodId'])
        shipping_methods_serializer = ShippingMethodSerializer(shipping_method, data=shipping_methods_data)
        if shipping_methods_serializer.is_valid():
            shipping_methods_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    @staticmethod
    def delete(id: int) -> JsonResponse:
        shipping_method = ShippingMethod.objects.get(ShippingMethodId=id)
        shipping_method.delete()
        return JsonResponse("Deleted Successfully", safe=False)
