# Generated by Django 3.2.2 on 2021-07-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20210720_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('1', 'With People'), ('2', 'Without People'), ('3', 'Room for Copy')], default='Without People', max_length=254),
        ),
        migrations.AddField(
            model_name='product',
            name='orientation',
            field=models.CharField(choices=[('P', 'Portrait'), ('L', 'Landscape'), ('S', 'Square')], default='Portrait', max_length=254),
        ),
    ]
