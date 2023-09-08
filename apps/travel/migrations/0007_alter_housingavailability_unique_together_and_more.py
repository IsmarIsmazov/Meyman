# Generated by Django 4.2.3 on 2023-09-08 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_housingreservation_adults_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='housingavailability',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='housingavailability',
            name='rooms',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='availability', to='travel.room', verbose_name='Номер'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='housingavailability',
            unique_together={('rooms', 'date')},
        ),
        migrations.RemoveField(
            model_name='housingavailability',
            name='housing',
        ),
    ]
