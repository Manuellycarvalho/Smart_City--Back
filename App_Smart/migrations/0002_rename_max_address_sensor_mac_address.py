# Generated by Django 4.2.13 on 2024-05-17 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Smart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='max_address',
            new_name='mac_address',
        ),
    ]
