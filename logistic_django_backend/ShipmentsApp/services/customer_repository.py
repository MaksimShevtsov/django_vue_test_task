from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ShipmentsApp.models import Customer
from ShipmentsApp.serializers import CustomerSerializer


class CustomerRepository(object):

    @staticmethod
    def get_all() -> JsonResponse:
        customer_data = Customer.objects.all()
        serializer = CustomerSerializer(customer_data, many=True)
        return JsonResponse(serializer.data, safe=False)

    @staticmethod
    def create(request: object) -> JsonResponse:
        customer_data = JSONParser().parse(request)
        customer_data_serializer = CustomerSerializer(data=customer_data)
        if customer_data_serializer.is_valid():
            customer_data_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    @staticmethod
    def update(request: object) -> JsonResponse:
        customer_data = JSONParser().parse(request)
        customer_method = Customer.objects.get(CustomerId=customer_data['CustomerId'])
        customer_methods_serializer = CustomerSerializer(customer_method, data=customer_data)
        if customer_methods_serializer.is_valid():
            customer_methods_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    @staticmethod
    def delete(id: int) -> JsonResponse:
        customer_method = Customer.objects.get(CustomerId=id)
        customer_method.delete()
        return JsonResponse("Deleted Successfully", safe=False)
