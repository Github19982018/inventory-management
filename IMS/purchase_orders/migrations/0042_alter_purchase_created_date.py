# Generated by Django 5.1.1 on 2024-09-13 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0041_alter_purchase_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 13, 15, 23, 18, 554140)),
        ),
    ]
