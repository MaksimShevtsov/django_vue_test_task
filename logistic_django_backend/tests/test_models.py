from django.test import TestCase

from shipments_app.models import ShippingMethod, Customer, Order


class ShippingMethodTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        ShippingMethod.objects.create(shipping_method_name='TrainTest')

    def test_first_shipping_method(self):
        method = ShippingMethod.objects.get(shipping_method_id=1)
        field_label = method._meta.get_field('shipping_method_name').verbose_name
        self.assertEquals(field_label, 'shipping_method_name')

    def test_firs_name_max_length(self):
        method = ShippingMethod.objects.get(shipping_method_id=1)
        max_length = method._meta.get_field('shipping_method_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_shipping(self):
        method = ShippingMethod.objects.get(shipping_method_id=1)
        expected_object_name = '%s, %s' % (method.shipping_method_id, method.shipping_method_name)
        self.assertEquals(expected_object_name, str(method))


class CustomerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(customer_name='Maxtest', customer_delivery_address='Lanowa 5A')

    def test_first_customer(self):
        customer = Customer.objects.get(customer_id=1)
        field_label = customer._meta.get_field('customer_name').verbose_name
        self.assertEquals(field_label, 'customer_name')

    def test_name_max_length(self):
        customer = Customer.objects.get(customer_id=1)
        max_length = customer._meta.get_field('customer_name').max_length
        self.assertEquals(max_length, 50)

    def test_address_max_length(self):
        customer = Customer.objects.get(customer_id=1)
        max_length = customer._meta.get_field('customer_delivery_address').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_customer(self):
        customer = Customer.objects.get(customer_id=1)
        expected_object_name = '%s, %s' % (customer.customer_name, customer.customer_delivery_address)
        self.assertEquals(expected_object_name, f'{customer.customer_name}, {customer.customer_delivery_address}')
