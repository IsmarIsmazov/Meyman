# Generated by Django 4.2.3 on 2023-08-05 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_accommodationreservation_check_in_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accommodationreservation',
            name='user',
        ),
        migrations.DeleteModel(
            name='AdminReview',
        ),
        migrations.RemoveField(
            model_name='carreservation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='AccommodationReservation',
        ),
        migrations.DeleteModel(
            name='CarReservation',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
