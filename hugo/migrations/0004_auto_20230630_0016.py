# Generated by Django 3.2.2 on 2023-06-30 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hugo', '0003_delete_hugo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Styles',
            },
        ),
        migrations.AddField(
            model_name='artwork',
            name='style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hugo.style'),
        ),
    ]
