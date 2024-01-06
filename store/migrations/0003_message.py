# Generated by Django 4.1.6 on 2024-01-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=277)),
                ('subject', models.CharField(max_length=200)),
                ('user_message', models.CharField(max_length=450)),
            ],
        ),
    ]
