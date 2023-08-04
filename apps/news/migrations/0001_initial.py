# Generated by Django 4.2.3 on 2023-08-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/news', verbose_name='Изображение новости')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка на источник')),
                ('is_favorite', models.BooleanField(blank=True, default=False, null=True, verbose_name='Добавить в избраное')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='человеко-понятный url')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
