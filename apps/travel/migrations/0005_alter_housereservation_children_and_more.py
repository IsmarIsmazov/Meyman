# Generated by Django 4.2.3 on 2023-08-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_alter_housereservation_housing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housereservation',
            name='children',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Дети(от 2-12 лет)'),
        ),
        migrations.AlterField(
            model_name='housereservation',
            name='teens',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Подростки(от 13-18 лет)'),
        ),
    ]
