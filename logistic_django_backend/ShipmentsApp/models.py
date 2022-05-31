from django.db import models


class ShippingMethod(models.Model):
    ShippingMethodId = models.AutoField(primary_key=True)
    ShippingMethodName = models.CharField(max_length=100)

    def __str__(self):
        return '%s, %s' % (self.ShippingMethodId, self.ShippingMethodName)


class Customer(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=50)
    CustomerDeliveryAddress = models.CharField(max_length=50)


class Order(models.Model):
    OrderId = models.AutoField(primary_key=True)
    ShippingDate = models.DateField()
    TrackingNo = models.IntegerField(unique=True)
    Status = models.BooleanField()
    Customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    ShippingMethod = models.ForeignKey(
        ShippingMethod,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.OrderId} ({self.Customer})'
