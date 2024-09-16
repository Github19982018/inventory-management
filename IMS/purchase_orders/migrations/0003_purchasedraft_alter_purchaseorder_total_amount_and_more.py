# Generated by Django 5.1.1 on 2024-09-15 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0002_alter_purchaseorder_contact_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseDraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseitems',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='purchase_orders.purchasedraft'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='order', serialize=False, to='purchase_orders.purchasedraft'),
        ),
        migrations.AlterField(
            model_name='purchasesitems',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='purchase_orders.purchasedraft'),
        ),
    ]
