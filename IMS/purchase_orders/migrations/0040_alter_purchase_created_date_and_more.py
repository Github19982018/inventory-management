# Generated by Django 5.1.1 on 2024-09-13 08:37

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0051_alter_inventory_updated'),
        ('purchase_orders', '0039_alter_purchase_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 13, 14, 7, 29, 434813)),
        ),
        migrations.AlterField(
            model_name='purchase_items',
            name='item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='inventory.inventory'),
        ),
    ]
