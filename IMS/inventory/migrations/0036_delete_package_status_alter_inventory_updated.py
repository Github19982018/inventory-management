# Generated by Django 5.1.1 on 2024-09-11 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0035_alter_inventory_updated'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Package_status',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 11, 11, 8, 13, 902386)),
        ),
    ]
