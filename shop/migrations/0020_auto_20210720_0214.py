# Generated by Django 3.2.2 on 2021-07-20 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20210720_0144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='label',
        ),
        migrations.RemoveField(
            model_name='product',
            name='orientation',
        ),
    ]
