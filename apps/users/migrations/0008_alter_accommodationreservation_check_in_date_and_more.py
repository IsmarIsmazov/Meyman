# Generated by Django 4.2.3 on 2023-07-24 06:24

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_accommodationreservation_booking_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodationreservation',
            name='check_in_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 7, 24))], verbose_name='Заезд'),
        ),
        migrations.AlterField(
            model_name='accommodationreservation',
            name='check_out_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 7, 24))], verbose_name='Выезд'),
        ),
        migrations.AlterField(
            model_name='carreservation',
            name='check_in_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 7, 24))], verbose_name='дата бронирование'),
        ),
        migrations.AlterField(
            model_name='carreservation',
            name='check_out_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 7, 24))]),
        ),
    ]
