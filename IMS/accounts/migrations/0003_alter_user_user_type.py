# Generated by Django 5.1.1 on 2024-09-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_address_remove_user_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Inventory Manager'), (2, 'Inventory Specialist')], null=True),
        ),
    ]
