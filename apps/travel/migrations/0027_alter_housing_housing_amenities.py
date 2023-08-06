# Generated by Django 4.2.3 on 2023-08-05 22:14

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0026_remove_room_image_room_bed_type_room_bedrooms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing',
            name='housing_amenities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('free_internet', 'Бесплатный интернет'), ('spa_services', 'Спа услуги'), ('restaurant', 'Ресторан'), ('Sports Hall', 'Спортивный зал'), ('pool', 'Бассейн'), ('airport_transfer', 'Трансфер от/до аэропорта'), ('fitness', 'Фитнес'), ('pet_allowed', 'Можно с питомцами'), ('indoor_pool', 'Крытый бассейн'), ('non_smoking_rooms', 'Номера для некурящих'), ('wifi', 'Wifi'), ('room_service', 'Доставка еды и напитков в номер'), ('coffee_teapot', 'Кофеварка/чайник'), ('bar', 'Бар'), ('garden_furniture', 'Садовая мебель'), ('sun_terrace', 'Терасса для загара'), ('garden', 'Сад'), ('wine_champagne', 'Вино/шампанское (платно)'), ('kids_menu', 'Детское меню (платно)'), ('breakfast_in_room', 'Завтрак в номер'), ('breakfast_paid', 'Завтрак включен в стоимость проживания?'), ('free_wifi', 'Бесплатный Wi-Fi на территории всего отеля'), ('daily_cleaning', 'Ежедневная уборка'), ('laundry_service', 'Услуги по глажению одежды (платно)'), ('paid_cleaning', 'Химчистка (платно)'), ('paid_laundry', 'Прачечная (платно)'), ('fax_xerox', 'Факс/ксерокопирование (платно)'), ('conference_banquet_hall', 'Конференц-зал/банкетный зал (платно)'), ('fire_extinguishers', 'Огнетушители'), ('smoke_detectors', 'Датчики дыма'), ('outdoor_surveillance', 'Видеонаблюдения снаружи здания'), ('public_areas_surveillance', 'Видеонаблюдения в местах общего пользования'), ('security_alarm', 'Охранная сигнализация'), ('full_time_security', 'Круглосуточная охрана'), ('safe', 'Сейф'), ('invoices_issued', 'Выдаются счета'), ('lockers', 'Запирающиеся шкафчики'), ('concierge_service', 'Услуги консьержа'), ('atm_on_site', 'Банкомат на территории отеля'), ('luggage_storage', 'Хранение багажа'), ('express_check_in', 'Ускоренная регистрация'), ('full_time_front_desk', 'Круглосуточная стойка регистрации'), ('transfer_paid', 'Трансфер (платно)'), ('food_delivery_to_room_paid', 'Доставка продуктов питания в номер (платно)'), ('smoking_areas', 'Места для курения'), ('air_conditioner', 'Кондиционер'), ('heating', 'Отопление'), ('car_rental', 'Прокат автомобилей'), ('packed_lunches', 'Упакованные ланчи'), ('ironing_facilities', 'Гладильные принадлежности'), ('buffet_breakfast', 'Завтрак "шведский стол"'), ('free_instant_coffee', 'Бесплатный растворимый кофе'), ('free_tea', 'Бесплатный чай'), ('happy_hour', 'Счастливый час'), ('special_diet_menu', 'Специальное диетическое меню'), ('taxi_service', 'Служба такси'), ('internet_business_center', 'Бизнес-центр с доступом в Интернет'), ('facial_treatments', 'Процедуры для лица'), ('foot_massage', 'Массаж ног'), ('full_body_massage', 'Массаж всего тела'), ('hammam', 'Хаммам'), ('manual_massage', 'Ручной массаж'), ('head_massage', 'Массаж головы'), ('massage', 'Массаж'), ('neck_massage', 'Массаж шеи'), ('steam_room', 'Паровая комната'), ('currency_exchange', 'Обмен валюты'), ('bell_staff_porter', 'Швейцар'), ('individual_check_in_check_out', 'Индивидуальная регистрация заезда/отъезда'), ('dry_cleaning', 'Сухая чистка'), ('shoe_shine', 'Чистка обуви'), ('kids_playground', 'Детская площадка'), ('allow_children', 'Можно c детьми'), ('allow_pets', 'C домашними животными'), ('pets_paid', 'Берете ли вы плату за домашних животных?'), ('Parking lot', 'Парковка')], max_length=100, verbose_name='Удобства в объекте'),
        ),
    ]