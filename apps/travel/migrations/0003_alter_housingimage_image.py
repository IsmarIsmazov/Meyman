# Generated by Django 4.2.3 on 2023-08-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housingimage',
            name='image',
            field=models.ImageField(upload_to='media/images/housing/', verbose_name='Изображение места жительства'),
        ),
    ]