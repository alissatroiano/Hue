# Generated by Django 3.2.2 on 2023-08-30 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hugo', '0009_style_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='in_import_queue',
            field=models.BooleanField(default=False),
        ),
    ]
