# Generated by Django 4.0.4 on 2022-06-02 22:16

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
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_delivery_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingMethod',
            fields=[
                ('shipping_method_id', models.AutoField(primary_key=True, serialize=False)),
                ('shipping_method_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('shipping_date', models.DateField()),
                ('tracking_no', models.IntegerField(unique=True)),
                ('status', models.BooleanField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shipments_app.customer')),
                ('shipping_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shipments_app.shippingmethod')),
            ],
        ),
    ]