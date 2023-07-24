# Generated by Django 4.2.3 on 2023-07-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_accommodationreservation_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodationreservation',
            name='booking_type',
            field=models.IntegerField(choices=[(1, 'Без банковской карты'), (2, 'Бесплатная отмена')], default=1, verbose_name='Бронирование'),
        ),
    ]
