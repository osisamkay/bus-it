# Generated by Django 5.0.2 on 2024-07-25 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_route_delete_routes'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='route',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]