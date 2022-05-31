from django.test import TestCase
from ShipmentsApp.models import ShippingMethod, Customer, Order
from ShipmentsApp.serializers import CustomerSerializer, ShippingMethodSerializer


class SerializerTest(TestCase):

    def setUp(self):
        shipments_method_data = {
            'ShippingMethodId': 1,
            'ShippingMethodName': 'Car'
        }

        self.shipping_method = ShippingMethod.objects.create(**shipments_method_data)
        self.ship_serializer = ShippingMethodSerializer(self.shipping_method, many=True)

    def test_contains_expected_fields(self):
        self.assertEqual(self.ship_serializer, self.shipping_method)
