# Generated by Django 4.2.3 on 2023-08-08 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_alter_housingimage_housing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='housingimage',
            options={},
        ),
        migrations.AddField(
            model_name='housing',
            name='images',
            field=models.ManyToManyField(related_name='housing_images', to='travel.housingimage', verbose_name='Images'),
        ),
        migrations.AddField(
            model_name='housingimage',
            name='image_type',
            field=models.CharField(choices=[('Photo', 'Photo'), ('Video', 'Video')], default=1, max_length=10, verbose_name='Image type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='housingimage',
            name='housing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.housing', verbose_name='Housing'),
        ),
        migrations.AlterField(
            model_name='housingimage',
            name='image',
            field=models.ImageField(upload_to='housing_images/', verbose_name='Housing Image'),
        ),
    ]
