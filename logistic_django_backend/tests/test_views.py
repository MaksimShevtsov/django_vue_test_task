import json

from django.test import TestCase

from shipments_app.models import ShippingMethod, Customer, Order


class ShippingMethodApiTest(TestCase):
    test_url = '/api/v1/shipping_methods'

    @classmethod
    def setUpTestData(cls):
        # Create 5 methods
        number_of_methods = 5
        for method_num in range(number_of_methods):
            ShippingMethod.objects.create(shipping_method_name='Train %s' % method_num)

    def test_get_all_methods(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)

    def test_post_methods(self):
        data = {
            'shipping_method_name': 'Traintest'
        }
        response = self.client.post(self.test_url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Added Successfully')

    def test_put_methods(self):
        data = {
            'shipping_method_id': 2,
            'shipping_method_name': 'Traintest1'
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
            Customer.objects.create(customer_name='Loe %s' % method_num,
                                    customer_delivery_address='Poland %s' % method_num)

    def test_get_all_methods(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)

    def test_post_methods(self):
        data = {
            'customer_name': 'MaxTest',
            'customer_delivery_address': '52-311 Poland'
        }
        response = self.client.post(self.test_url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Added Successfully')

    def test_put_methods(self):
        data = {
            'customer_id': 2,
            'customer_name': 'MaxTest2',
            'customer_delivery_address': '52-311 USA'
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
#         Order.objects.create(shipping_date='2020-08-08',
#                              tracking_no=1111111111,
#                              status=True,
#                              customer_id='1',
#                              shipping_method_id='1')
#
#     def test_get_all_methods(self):
#         response = self.client.get(self.test_url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_post_methods(self):
#         data = {
#             'shipping_date': '2020-08-08',
#             'tracking_no': 1234567,
#             'status': False,
#             'customer_id': 1,
#             'shipping_method_id': 1
#         }
#         response = self.client.post(self.test_url, data=json.dumps(data), content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), 'Added Successfully')
#
#     def test_put_methods(self):
#         data = {
#             'order_id': 2,
#             'shipping_date': '2020-08-08',
#             'tracking_no': 1234567,
#             'status': False,
#             'customer_id': 1,
#             'shipping_method_id': 1
#         }
#         response = self.client.put(self.test_url, data=json.dumps(data), content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), 'Updated Successfully')
#
#     def test_delete_methods(self):
#         response = self.client.delete('/api/v1/order/2')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), 'Deleted Successfully')
