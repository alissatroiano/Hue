# Generated by Django 3.2.2 on 2023-05-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hugo', '0004_auto_20230525_1451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hugo',
            options={'verbose_name_plural': 'Hugos'},
        ),
        migrations.AddField(
            model_name='hugo',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
