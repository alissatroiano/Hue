# Generated by Django 3.2.2 on 2021-06-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
