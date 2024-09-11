# Generated by Django 5.1.1 on 2024-09-11 05:38

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0036_delete_package_status_alter_inventory_updated'),
        ('sales_orders', '0009_alter_sales_created_date_alter_sales_status_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='sales',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 11, 11, 8, 13, 920877)),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slip', models.PositiveIntegerField(auto_created=True)),
                ('created_at', models.DateTimeField()),
                ('packed_at', models.DateTimeField()),
                ('shipping_address', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.customer')),
                ('sales', models.ManyToManyField(to='sales_orders.sales')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales_orders.package_status')),
            ],
        ),
    ]
