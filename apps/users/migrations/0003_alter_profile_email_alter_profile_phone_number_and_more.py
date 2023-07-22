# Generated by Django 4.2.3 on 2023-07-22 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel_service', '0001_initial'),
        ('travel', '0005_alter_housing_is_favorite'),
        ('users', '0002_remove_reservation_reserve_profile_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='Номер телефона'),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choise', models.CharField(choices=[('Отели', 'Отели'), ('Хостелы', 'Хостелы'), ('Апартаменты', 'Апартаменты'), ('Гостевые дома', 'Гостевые дома'), ('Санатории', 'Санатории')], max_length=250)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.housing')),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_service.transfer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
