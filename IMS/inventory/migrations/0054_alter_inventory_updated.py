# Generated by Django 5.1.1 on 2024-09-13 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0053_alter_inventory_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 13, 18, 10, 57, 105136)),
        ),
    ]
