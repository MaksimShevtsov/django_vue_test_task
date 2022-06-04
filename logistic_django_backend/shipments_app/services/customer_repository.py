from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from shipments_app.models import Customer
from shipments_app.serializers import CustomerSerializer


class CustomerRepository:

    @staticmethod
    def get_all() -> Response:
        customer_data = Customer.objects.all()
        serializer = CustomerSerializer(customer_data, many=True)
        return Response(serializer.data)

    @staticmethod
    def create(request: object) -> Response:
        customer_data = JSONParser().parse(request)
        customer_data_serializer = CustomerSerializer(data=customer_data)
        if customer_data_serializer.is_valid():
            customer_data_serializer.save()
            return Response("Added Successfully")
        return Response("Failed to Add")

    @staticmethod
    def update(request: object) -> Response:
        customer_data = JSONParser().parse(request)
        customer_method = Customer.objects.get(customer_id=customer_data['customer_id'])
        customer_methods_serializer = CustomerSerializer(customer_method, data=customer_data)
        if customer_methods_serializer.is_valid():
            customer_methods_serializer.save()
            return Response("Updated Successfully")
        return Response("Failed to Update")

    @staticmethod
    def delete(id: int) -> Response:
        customer_method = Customer.objects.get(customer_id=id)
        customer_method.delete()
        return Response("Deleted Successfully")
