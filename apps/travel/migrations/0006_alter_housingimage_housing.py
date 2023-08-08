# Generated by Django 4.2.3 on 2023-08-08 10:11

import apps.travel.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_remove_housing_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housingimage',
            name='housing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house_images', to='travel.housing'),
        ),
    ]
