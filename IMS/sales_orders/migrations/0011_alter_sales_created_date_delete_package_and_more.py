# Generated by Django 5.1.1 on 2024-09-11 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_orders', '0010_package_status_alter_sales_created_date_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 11, 11, 17, 34, 626881)),
        ),
        migrations.DeleteModel(
            name='Package',
        ),
        migrations.DeleteModel(
            name='Package_status',
        ),
    ]
