# Generated by Django 3.2.2 on 2023-08-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hugo', '0004_auto_20230630_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='is_downloadable',
            field=models.BooleanField(default=False),
        ),
    ]
