from django.test import TestCase

from ShipmentsApp.models import ShippingMethod, Customer, Order


class ShippingMethodTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        ShippingMethod.objects.create(ShippingMethodName='TrainTest')

    def test_first_shipping_method(self):
        method = ShippingMethod.objects.get(ShippingMethodId=1)
        field_label = method._meta.get_field('ShippingMethodName').verbose_name
        self.assertEquals(field_label, 'ShippingMethodName')

    def test_firs_name_max_length(self):
        method = ShippingMethod.objects.get(ShippingMethodId=1)
        max_length = method._meta.get_field('ShippingMethodName').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_shipping(self):
        method = ShippingMethod.objects.get(ShippingMethodId=1)
        expected_object_name = '%s, %s' % (method.ShippingMethodId, method.ShippingMethodName)
        self.assertEquals(expected_object_name, str(method))


class CustomerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(CustomerName='Maxtest', CustomerDeliveryAddress='Lanowa 5A')

    def test_first_customer(self):
        customer = Customer.objects.get(CustomerId=1)
        field_label = customer._meta.get_field('CustomerName').verbose_name
        self.assertEquals(field_label, 'CustomerName')

    def test_name_max_length(self):
        customer = Customer.objects.get(CustomerId=1)
        max_length = customer._meta.get_field('CustomerName').max_length
        self.assertEquals(max_length, 50)

    def test_address_max_length(self):
        customer = Customer.objects.get(CustomerId=1)
        max_length = customer._meta.get_field('CustomerDeliveryAddress').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_customer(self):
        customer = Customer.objects.get(CustomerId=1)
        expected_object_name = '%s, %s' % (customer.CustomerName, customer.CustomerDeliveryAddress)
        self.assertEquals(expected_object_name, f'{customer.CustomerName}, {customer.CustomerDeliveryAddress}')
