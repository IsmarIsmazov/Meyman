# Generated by Django 4.2.3 on 2023-08-10 18:50

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0013_alter_housing_housing_amenities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_amenities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Кондиционер', 'Кондиционер'), ('Фен', 'Фен'), ('Стиральная машина', 'Стиральная машина'), ('Утюг', 'Утюг'), ('Сушильная машина', 'Сушильная машина'), ('Холодильник', 'Холодильник'), ('Телевизор', 'Телевизор'), ('Микроволновка', 'Микроволновка'), ('Отопление', 'Отопление'), ('Диван-кровать', 'Диван-кровать'), ('Раскладная кровать', 'Раскладная кровать'), ('Двуспальная кровать', 'Двуспальная кровать'), ('Шкаф или гардероб', 'Шкаф или гардероб'), ('Белье', 'Белье'), ('Вешалка для одежды', 'Вешалка для одежды'), ('Бесплатные туалетно-косметические принадлежности', 'Бесплатные туалетно-косметические принадлежности'), ('Туалетная бумага', 'Туалетная бумага'), ('Кухонные принадлежности', 'Кухонные принадлежности'), ('Электрический чайник', 'Электрический чайник'), ('Вид на город', 'Вид на город'), ('Вид на сад', 'Вид на сад'), ('Высокий туалет', 'Высокий туалет'), ('Туалет с поручнями', 'Туалет с поручнями'), ('Подходит для гостей с ограниченными возможностями', 'Подходит для гостей с ограниченными возможностями'), ('Рабочий стол', 'Рабочий стол'), ('Уборка', 'Уборка'), ('Кофеварка/чайник', 'Кофеварка/чайник'), ('Кабельное / спутниковое телевидение', 'Кабельное / спутниковое телевидение'), ('Биде', 'Биде'), ('Доступны смежные номера', 'Доступны смежные номера'), ('Обслуживание номеров', 'Обслуживание номеров'), ('Безопасный', 'Безопасный'), ('Зона отдыха', 'Зона отдыха'), ('Телефон', 'Телефон'), ('Бутилированная вода', 'Бутилированная вода'), ('Сейф', 'Сейф'), ('Сейф для ноутбука', 'Сейф для ноутбука'), ('Частные ванные комнаты', 'Частные ванные комнаты'), ('Услуга будильник / будильник', 'Услуга будильник / будильник'), ('Минибар', 'Минибар'), ('Ванна/душ', 'Ванна/душ'), ('Комоды', 'Комоды'), ('Мини кухня', 'Мини кухня'), ('Камин', 'Камин'), ('Закуски', 'Закуски'), ('2 комнаты', '2 комнаты'), ('Тумба', 'Тумба'), ('Телевизор', 'Телевизор'), ('Ванная комната', 'Ванная комната'), ('Телефон', 'Телефон'), ('Комоды', 'Комоды'), ('Тапочки', 'Тапочки'), ('Халат', 'Халат')], max_length=850, verbose_name='Удобства'),
        ),
    ]
