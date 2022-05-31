# Generated by Django 4.0.4 on 2022-05-29 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('CustomerId', models.AutoField(primary_key=True, serialize=False)),
                ('CustomerName', models.CharField(max_length=50)),
                ('CustomerDeliveryAddress', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingMethod',
            fields=[
                ('ShippingMethodId', models.AutoField(primary_key=True, serialize=False)),
                ('ShippingMethodName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderId', models.AutoField(primary_key=True, serialize=False)),
                ('ShippingDate', models.DateField()),
                ('Delivery', models.CharField(max_length=250)),
                ('TrackingNo', models.IntegerField()),
                ('Status', models.BooleanField()),
                ('Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Orders', to='ShipmentsApp.customer')),
                ('ShippingMethod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Orders_ship', to='ShipmentsApp.shippingmethod')),
            ],
        ),
    ]
