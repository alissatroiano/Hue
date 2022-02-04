# Generated by Django 3.2.2 on 2022-02-04 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artistinfo',
            old_name='artist',
            new_name='user',
        ),
        migrations.AddField(
            model_name='artistinfo',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='artistinfo',
            name='name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
