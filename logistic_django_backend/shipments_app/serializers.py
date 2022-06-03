from rest_framework import serializers
from shipments_app.models import ShippingMethod, Customer, Order


class ShippingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingMethod
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(Customer)
    shipping_method = ShippingMethodSerializer(ShippingMethod)

    class Meta:
        model = Order
        fields = '__all__'


class OrderPostSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(read_only=False)
    shipping_method_id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Order
        fields = ('order_id', 'shipping_date', 'tracking_no', 'status', 'customer_id', 'shipping_method_id')
