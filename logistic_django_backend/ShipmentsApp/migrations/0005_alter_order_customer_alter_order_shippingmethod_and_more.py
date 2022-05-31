# Generated by Django 4.0.4 on 2022-05-30 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShipmentsApp', '0004_rename_customer_id_order_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Customer',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='ShipmentsApp.customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='ShippingMethod',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='ShipmentsApp.shippingmethod'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='TrackingNo',
            field=models.IntegerField(unique=True),
        ),
    ]