# Generated by Django 4.2.3 on 2023-08-08 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_alter_housingimage_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housingimage',
            name='image',
        ),
    ]
