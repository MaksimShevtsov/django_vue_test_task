from django.test import TestCase
from shipments_app.models import ShippingMethod, Customer, Order
from shipments_app.serializers import CustomerSerializer, ShippingMethodSerializer


class SerializerTest(TestCase):

    def setUp(self):
        shipments_method_data = {
            'shipping_method_id': 1,
            'shipping_method_name': 'Car'
        }

        self.shipping_method = ShippingMethod.objects.create(**shipments_method_data)
        self.ship_serializer = ShippingMethodSerializer(self.shipping_method, many=True)

    def test_contains_expected_fields(self):
        self.assertEqual(self.ship_serializer, self.shipping_method)
