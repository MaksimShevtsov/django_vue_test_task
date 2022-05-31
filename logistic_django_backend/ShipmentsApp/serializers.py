from rest_framework import serializers
from ShipmentsApp.models import ShippingMethod, Customer, Order


class ShippingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingMethod
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(source='Customer')
    shipping = ShippingMethodSerializer(source='ShippingMethod')

    class Meta:
        model = Order
        fields = '__all__'


class OrderPostSerializer(serializers.ModelSerializer):
    Customer_id = serializers.IntegerField(read_only=False)
    ShippingMethod_id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Order
        fields = ('OrderId', 'ShippingDate', 'TrackingNo', 'Status', 'Customer_id', 'ShippingMethod_id')
