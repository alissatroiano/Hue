# Generated by Django 3.2.2 on 2021-06-03 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
    ]
