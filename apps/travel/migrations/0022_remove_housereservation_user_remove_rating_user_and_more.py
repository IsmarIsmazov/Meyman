# Generated by Django 4.2.3 on 2023-08-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0021_alter_roomimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housereservation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.AlterField(
            model_name='roomimage',
            name='image',
            field=models.ImageField(null=True, upload_to='images/rooms/', verbose_name='Изображение номера'),
        ),
    ]
