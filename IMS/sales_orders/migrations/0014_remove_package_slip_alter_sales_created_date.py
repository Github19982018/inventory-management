# Generated by Django 5.1.1 on 2024-09-11 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_orders', '0013_remove_package_sales_alter_sales_created_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='slip',
        ),
        migrations.AlterField(
            model_name='sales',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 11, 12, 33, 38, 127942)),
        ),
    ]
