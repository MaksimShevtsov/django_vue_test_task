from django.db import models


class ShippingMethod(models.Model):
    shipping_method_id = models.AutoField(primary_key=True)
    shipping_method_name = models.CharField(max_length=100)

    def __str__(self):
        return '%s, %s' % (self.shipping_method_id, self.shipping_method_name)


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_delivery_address = models.CharField(max_length=50)

    def __str__(self):
        return '%s, %s' % (self.customer_id, self.customer_delivery_address)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    shipping_date = models.DateField()
    tracking_no = models.IntegerField(unique=True)
    status = models.BooleanField()
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        null=True,
    )
    shipping_method = models.ForeignKey(
        ShippingMethod,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.order_id} ({self.customer})'
