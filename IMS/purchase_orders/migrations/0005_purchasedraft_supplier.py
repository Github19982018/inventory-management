# Generated by Django 5.1.1 on 2024-09-15 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0004_remove_purchaseitems_supplier_and_more'),
        ('supplier', '0008_alter_supplier_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedraft',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='supplier.supplier'),
        ),
    ]
