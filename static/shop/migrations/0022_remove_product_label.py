# Generated by Django 3.2.2 on 2021-07-20 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_product_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='label',
        ),
    ]
