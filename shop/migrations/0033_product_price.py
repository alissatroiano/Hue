# Generated by Django 3.2.2 on 2021-07-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_auto_20210726_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
