# Generated by Django 5.1.1 on 2024-09-11 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0042_delete_ship_status_alter_inventory_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 11, 13, 15, 48, 788797)),
        ),
    ]
