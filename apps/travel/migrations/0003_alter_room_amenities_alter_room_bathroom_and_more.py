# Generated by Django 4.2.3 on 2023-08-23 12:53

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='amenities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Балкон', 'Балкон'), ('Терраса', 'Терраса'), ('Вид из окна', 'Вид из окна')], max_length=255, verbose_name='На улице'),
        ),
        migrations.AlterField(
            model_name='room',
            name='bathroom',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Душ', 'Душ'), ('Туалетная бумага', 'Туалетная бумага'), ('Туалет', 'Туалет'), ('Фен', 'Фен'), ('Ванна', 'Ванна'), ('Бесплатные уходовые средства', 'Бесплатные уходовые средства'), ('Биде', 'Биде'), ('Тапочки', 'Тапочки'), ('Халат', 'Халат')], max_length=255, verbose_name='Ванная'),
        ),
        migrations.AlterField(
            model_name='room',
            name='kitchen',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('чайник', 'Электронный чайник'), ('микроволновка', 'Микроволновка'), ('обеденный_стол', 'Обеденный стол'), ('кофеварка', 'Кофеварка'), ('mini_bar', 'Mini-bar'), ('холодильник', 'Холодильник')], max_length=255, verbose_name='Кухня'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_amenities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Двуспальная кровать', 'Двуспальная кровать'), ('Кондиционер', 'Кондиционер'), ('Тумба', 'Тумба'), ('Телевизор', 'Телевизор'), ('Стиральная машина', 'Стиральная машина'), ('Ванная комната', 'Ванная комната'), ('Утюг', 'Утюг'), ('2 комнаты', '2 комнаты'), ('Холодильник', 'Холодильник'), ('Фен', 'Фен'), ('Сейф', 'Сейф'), ('Телефон', 'Телефон'), ('Комоды', 'Комоды'), ('Шкафы', 'Шкафы'), ('Мини кухня', 'Мини кухня'), ('Тапочки', 'Тапочки'), ('Халат', 'Халат'), ('Закуски', 'Закуски'), ('Камин', 'Камин')], max_length=255, verbose_name='Удобства'),
        ),
    ]