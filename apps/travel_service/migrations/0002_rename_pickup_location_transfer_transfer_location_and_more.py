# Generated by Django 4.2.3 on 2023-07-21 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfer',
            old_name='pickup_location',
            new_name='transfer_location',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='search',
        ),
    ]
