# Generated by Django 4.1.6 on 2024-01-01 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='state',
            new_name='phone',
        ),
    ]