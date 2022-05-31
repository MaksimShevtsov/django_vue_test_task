import json

from django.test import TestCase

from ShipmentsApp.models import ShippingMethod, Customer, Order


class ShippingMethodApiTest(TestCase):
    test_url = '/api/v1/shipping_method'

    @classmethod
    def setUpTestData(cls):
        # Create 5 methods
        number_of_methods = 5
        for method_num in range(number_of_methods):
            ShippingMethod.objects.create(ShippingMethodName='Train %s' % method_num)

    def test_get_all_methods(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)

    def test_post_methods(self):
        data = {
            'ShippingMethodName': 'Traintest'
        }
        response = self.client.post(self.test_url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Added Successfully')

    def test_put_methods(self):
        data = {
            'ShippingMethodId': 2,
            'ShippingMethodName': 'Traintest1'
        }
        response = self.client.put(self.test_url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Updated Successfully')

    def test_delete_methods(self):
        response = self.client.delete(f'{self.test_url}' + '/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Deleted Successfully')


class CustomerApiTest(TestCase):
    test_url = '/api/v1/customers'

    @classmethod
    def setUpTestData(cls):
        # Create 5 methods
        number_of_methods = 5
        for method_num in range(number_of_methods):
            Customer.objects.create(CustomerName='Loe %s' % method_num,
                                    CustomerDeliveryAddress='Poland %s' % method_num)

    def test_get_all_methods(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)

    def test_post_methods(self):
        data = {
            'CustomerName': 'MaxTest',
            'CustomerDeliveryAddress': '52-311 Poland'
        }
        response = self.client.post(self.test_url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Added Successfully')

    def test_put_methods(self):
        data = {
            'CustomerId': 2,
            'CustomerName': 'MaxTest2',
            'CustomerDeliveryAddress': '52-311 USA'
        }
        response = self.client.put(self.test_url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Updated Successfully')

    def test_delete_methods(self):
        response = self.client.delete('/api/v1/customer/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Deleted Successfully')


# class OrderApiTest(TestCase):
#     test_url = '/api/v1/orders'
#
#     @classmethod
#     def setUpTestData(cls):
#         Order.objects.create(ShippingDate='2020-08-08',
#                              TrackingNo=1111111111,
#                              Status=True,
#                              Customer_id='1',
#                              ShippingMethod_id='1')
#
#     def test_get_all_methods(self):
#         response = self.client.get(self.test_url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_post_methods(self):
#         data = {
#             'ShippingDate': '2020-08-08',
#             'TrackingNo': 1234567,
#             'Status': False,
#             'Customer_id': 1,
#             'ShippingMethod_id': 1
#         }
#         response = self.client.post(self.test_url, data=json.dumps(data), content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), 'Added Successfully')
#
#     def test_put_methods(self):
#         data = {
#             'OrderId': 2,
#             'ShippingDate': '2020-08-08',
#             'TrackingNo': 1234567,
#             'Status': False,
#             'Customer_id': 1,
#             'ShippingMethod_id': 1
#         }
#         response = self.client.put(self.test_url, data=json.dumps(data), content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), 'Updated Successfully')
#
#     def test_delete_methods(self):
#         response = self.client.delete('/api/v1/order/2')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), 'Deleted Successfully')
