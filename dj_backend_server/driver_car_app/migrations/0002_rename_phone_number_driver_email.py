# Generated by Django 3.2.5 on 2021-07-21 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver_car_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='phone_number',
            new_name='email',
        ),
    ]