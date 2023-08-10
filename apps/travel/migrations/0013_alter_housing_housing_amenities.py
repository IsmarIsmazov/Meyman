# Generated by Django 4.2.3 on 2023-08-10 18:47

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0012_alter_housingreservation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing',
            name='housing_amenities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Бесплатный интернет', 'Бесплатный интернет'), ('Спа услуги', 'Спа услуги'), ('Ресторан', 'Ресторан'), ('Спортивный зал', 'Спортивный зал'), ('Бассейн', 'Бассейн'), ('Трансфер от/до аэропорта', 'Трансфер от/до аэропорта'), ('Фитнес', 'Фитнес'), ('Крытый бассейн', 'Крытый бассейн'), ('Номера для некурящих', 'Номера для некурящих'), ('Wifi', 'Wifi'), ('Доставка еды и напитков в номер', 'Доставка еды и напитков в номер'), ('Кофеварка/чайник', 'Кофеварка/чайник'), ('Бар', 'Бар'), ('Садовая мебель', 'Садовая мебель'), ('Терасса для загара', 'Терасса для загара'), ('Сад', 'Сад'), ('Вино/шампанское (платно)', 'Вино/шампанское (платно)'), ('Детское меню (платно)', 'Детское меню (платно)'), ('Завтрак в номер', 'Завтрак в номер'), ('Завтрак включен в стоимость проживания?', 'Завтрак включен в стоимость проживания?'), ('Бесплатный Wi-Fi на территории всего отеля', 'Бесплатный Wi-Fi на территории всего отеля'), ('Ежедневная уборка', 'Ежедневная уборка'), ('Услуги по глажению одежды (платно)', 'Услуги по глажению одежды (платно)'), ('Химчистка (платно)', 'Химчистка (платно)'), ('Прачечная (платно)', 'Прачечная (платно)'), ('Факс/ксерокопирование (платно)', 'Факс/ксерокопирование (платно)'), ('Конференц-зал/банкетный зал (платно)', 'Конференц-зал/банкетный зал (платно)'), ('Огнетушители', 'Огнетушители'), ('Датчики дыма', 'Датчики дыма'), ('Видеонаблюдения снаружи здания', 'Видеонаблюдения снаружи здания'), ('Видеонаблюдения в местах общего пользования', 'Видеонаблюдения в местах общего пользования'), ('Охранная сигнализация', 'Охранная сигнализация'), ('Круглосуточная охрана', 'Круглосуточная охрана'), ('Сейф', 'Сейф'), ('Выдаются счета', 'Выдаются счета'), ('Запирающиеся шкафчики', 'Запирающиеся шкафчики'), ('Услуги консьержа', 'Услуги консьержа'), ('Банкомат на территории отеля', 'Банкомат на территории отеля'), ('Хранение багажа', 'Хранение багажа'), ('Ускоренная регистрация', 'Ускоренная регистрация'), ('Круглосуточная стойка регистрации', 'Круглосуточная стойка регистрации'), ('Трансфер (платно)', 'Трансфер (платно)'), ('Доставка продуктов питания в номер (платно)', 'Доставка продуктов питания в номер (платно)'), ('Места для курения', 'Места для курения'), ('Кондиционер', 'Кондиционер'), ('Отопление', 'Отопление'), ('Прокат автомобилей', 'Прокат автомобилей'), ('Упакованные ланчи', 'Упакованные ланчи'), ('Гладильные принадлежности', 'Гладильные принадлежности'), ('Завтрак "шведский стол"', 'Завтрак "шведский стол"'), ('Бесплатный растворимый кофе', 'Бесплатный растворимый кофе'), ('Бесплатный чай', 'Бесплатный чай'), ('Счастливый час', 'Счастливый час'), ('Специальное диетическое меню', 'Специальное диетическое меню'), ('Служба такси', 'Служба такси'), ('Бизнес-центр с доступом в Интернет', 'Бизнес-центр с доступом в Интернет'), ('Процедуры для лица', 'Процедуры для лица'), ('Массаж ног', 'Массаж ног'), ('Массаж всего тела', 'Массаж всего тела'), ('Хаммам', 'Хаммам'), ('Ручной массаж', 'Ручной массаж'), ('Массаж головы', 'Массаж головы'), ('Массаж', 'Массаж'), ('Массаж шеи', 'Массаж шеи'), ('Паровая комната', 'Паровая комната'), ('Обмен валюты', 'Обмен валюты'), ('Швейцар', 'Швейцар'), ('Индивидуальная регистрация заезда/отъезда', 'Индивидуальная регистрация заезда/отъезда'), ('Сухая чистка', 'Сухая чистка'), ('Чистка обуви', 'Чистка обуви'), ('Детская площадка', 'Детская площадка'), ('Можно c детьми', 'Можно c детьми'), ('C домашними животными', 'C домашними животными'), ('Берете ли вы плату за домашних животных?', 'Берете ли вы плату за домашних животных?'), ('Парковка', 'Парковка'), ('Джакузи', 'Джакузи'), ('Сауна', 'Сауна'), ('Камера хранения багажа', 'Камера хранения багажа'), ('Доступ людям с ограниченными возможностями', 'Доступ людям с ограниченными возможностями'), ('Сувенирный магазин', 'Сувенирный магазин'), ('Доступ в интернет: в номерах', 'Доступ в интернет: в номерах'), ('Доступ в интернет: на всей территории отеля', 'Доступ в интернет: на всей территории отеля'), ('Прокат автомобиля', 'Прокат автомобиля'), ('Питание', 'Питание'), ('Бар у бассейна', 'Бар у бассейна'), ('Кафе', 'Кафе')], max_length=1800, verbose_name='Удобства'),
        ),
    ]
