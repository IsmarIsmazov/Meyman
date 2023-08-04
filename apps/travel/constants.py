HOUSING_CHOICES = (
    ('Отели', 'Отели'),
    ('Хостелы', 'Хостелы'),
    ('Апартаменты', 'Апартаменты'),
    ('Гостевые дома', 'Гостевые дома'),
    ('Санатории', 'Санатории'),
)

ACCOMMODATION_CHOICES = (
    ("Жилье целиком", "Жилье целиком"),
    ("Комната", "Комната"),
    ("Общая комната", "Общая комната"),
)

BEDROOM_CHOICES = (
    ("1 спальня", "1 спальня"),
    ("2 спальни", "2 спальни"),
    ("Больше 3 спален", "Больше 3 спален"),
)

BED_CHOICES = (
    ("Отдельные", "Отдельные"),
    ("Двуспальная", "Двуспальная"),
    ("Больше 3х", "Больше 3х"),
    ("Kingsize", "Kingsize"),
    ("Queensize ", "Queensize "),
)

FOOD_CHOICES = (
    ("Все включено", "Все включено"),
    ("Завтрак включен", "Завтрак включен"),
    ("Не включено", "Не включено"),
    ("С собственной кухней", "С собственной кухней"),
)

PARKING_CHOICES = (
    ('free', 'Да, бесплатно'),
    ('paid', 'Да, платно'),
    ('no', 'Нет')
)

PARKING_LOCATION_CHOICES = (
    ('На территории', 'На территории'),
    ('За территорией', 'За территорией'),
)

PAYMENT_CHOICES = (
    ("К оплате сейчас", "К оплате сейчас"),
    ("Предоплата", "Предоплата"),
    ("Оплата наличными", "Оплата наличными"),
)

HOUSING_AMENITIES_CHOICES = (
    ('free_internet', 'Бесплатный интернет'),
    ('spa_services', 'Спа услуги'),
    ('restaurant', 'Ресторан'),
    ('Спортивный зал', 'Спортивный зал'),
    ('pool', 'Бассейн'),
    ('airport_transfer', 'Трансфер от/до аэропорта'),
    ('fitness', 'Фитнес'),
    ('pet_allowed', 'Можно с питомцами'),
    ('indoor_pool', 'Крытый бассейн'),
    ('non_smoking_rooms', 'Номера для некурящих'),
    ('wifi', 'Wifi'),
    ('room_service', 'Доставка еды и напитков в номер'),
    ('coffee_teapot', 'Кофеварка/чайник'),
    ('bar', 'Бар'),
    ('garden_furniture', 'Садовая мебель'),
    ('sun_terrace', 'Терасса для загара'),
    ('garden', 'Сад'),
    ('wine_champagne', 'Вино/шампанское (платно)'),
    ('kids_menu', 'Детское меню (платно)'),
    ('breakfast_in_room', 'Завтрак в номер'),
    ('breakfast_paid', 'Завтрак включен в стоимость проживания?'),
    ('free_wifi', 'Бесплатный Wi-Fi на территории всего отеля'),
    ('daily_cleaning', 'Ежедневная уборка'),
    ('laundry_service', 'Услуги по глажению одежды (платно)'),
    ('paid_cleaning', 'Химчистка (платно)'),
    ('paid_laundry', 'Прачечная (платно)'),
    ('fax_xerox', 'Факс/ксерокопирование (платно)'),
    ('conference_banquet_hall', 'Конференц-зал/банкетный зал (платно)'),
    ('fire_extinguishers', 'Огнетушители'),
    ('smoke_detectors', 'Датчики дыма'),
    ('outdoor_surveillance', 'Видеонаблюдения снаружи здания'),
    ('public_areas_surveillance', 'Видеонаблюдения в местах общего пользования'),
    ('security_alarm', 'Охранная сигнализация'),
    ('full_time_security', 'Круглосуточная охрана'),
    ('safe', 'Сейф'),
    ('invoices_issued', 'Выдаются счета'),
    ('lockers', 'Запирающиеся шкафчики'),
    ('concierge_service', 'Услуги консьержа'),
    ('atm_on_site', 'Банкомат на территории отеля'),
    ('luggage_storage', 'Хранение багажа'),
    ('express_check_in', 'Ускоренная регистрация'),
    ('full_time_front_desk', 'Круглосуточная стойка регистрации'),
    ('transfer_paid', 'Трансфер (платно)'),
    ('food_delivery_to_room_paid', 'Доставка продуктов питания в номер (платно)'),
    ('smoking_areas', 'Места для курения'),
    ('air_conditioner', 'Кондиционер'),
    ('heating', 'Отопление'),
    ('car_rental', 'Прокат автомобилей'),
    ('packed_lunches', 'Упакованные ланчи'),
    ('ironing_facilities', 'Гладильные принадлежности'),
    ('buffet_breakfast', 'Завтрак "шведский стол"'),
    ('free_instant_coffee', 'Бесплатный растворимый кофе'),
    ('free_tea', 'Бесплатный чай'),
    ('happy_hour', 'Счастливый час'),
    ('special_diet_menu', 'Специальное диетическое меню'),
    ('taxi_service', 'Служба такси'),
    ('internet_business_center', 'Бизнес-центр с доступом в Интернет'),
    ('facial_treatments', 'Процедуры для лица'),
    ('foot_massage', 'Массаж ног'),
    ('full_body_massage', 'Массаж всего тела'),
    ('hammam', 'Хаммам'),
    ('manual_massage', 'Ручной массаж'),
    ('head_massage', 'Массаж головы'),
    ('massage', 'Массаж'),
    ('neck_massage', 'Массаж шеи'),
    ('steam_room', 'Паровая комната'),
    ('currency_exchange', 'Обмен валюты'),
    ('bell_staff_porter', 'Швейцар'),
    ('individual_check_in_check_out', 'Индивидуальная регистрация заезда/отъезда'),
    ('dry_cleaning', 'Сухая чистка'),
    ('shoe_shine', 'Чистка обуви'),
    ('kids_playground', 'Детская площадка'),
    ('allow_children', 'C детьми?'),
    ('allow_pets', 'C домашними животными'),
    ('pets_paid', 'Берете ли вы плату за домашних животных?'),
    ('Парковка', 'Парковка'),
)

ROOM_AMENITIES_CHOICES = (
    ('air_conditioner', 'Кондиционер'),
    ('hair_dryer', 'Фен'),
    ('washing_machine', 'Стиральная машина'),
    ('iron', 'Утюг'),
    ('dryer', 'Сушильная машина'),
    ('fridge', 'Холодильник'),
    ('tv', 'Телевизор'),
    ('microwave', 'Микроволновка'),
    ('heating', 'Отопление'),
    ('sofa_bed', 'Диван-кровать'),
    ('folding_bed', 'Раскладная кровать'),
    ('Двуспальная кровать', 'Двуспальная кровать'),
    ('wardrobe', 'Шкаф или гардероб'),
    ('linen', 'Белье'),
    ('clothes_hanger', 'Вешалка для одежды'),
    ('complimentary_toiletries', 'Бесплатные туалетно-косметические принадлежности'),
    ('toilet_paper', 'Туалетная бумага'),
    ('kitchen_utensils', 'Кухонные принадлежности'),
    ('electric_kettle', 'Электрический чайник'),
    ('city_view', 'Вид на город'),
    ('garden_view', 'Вид на сад'),
    ('high_toilet', 'Высокий туалет'),
    ('toilet_with_handles', 'Туалет с поручнями'),
    ('accessible_to_disabled_guests', 'Подходит для гостей с ограниченными возможностями'),
    ('work_desk', 'Рабочий стол'),
    ('room_cleaning', 'Уборка'),
    ('coffee_teapot', 'Кофеварка/чайник'),
    ('cable_satellite_tv', 'Кабельное / спутниковое телевидение'),
    ('bidet', 'Биде'),
    ('connecting_rooms_available', 'Доступны смежные номера'),
    ('room_service', 'Обслуживание номеров'),
    ('safe', 'Безопасный'),
    ('sitting_area', 'Зона отдыха'),
    ('telephone', 'Телефон'),
    ('bottled_water', 'Бутилированная вода'),
    ('Сейф', 'Сейф'),
    ('laptop_safe_box', 'Сейф для ноутбука'),
    ('private_bathroom', 'Частные ванные комнаты'),
    ('wake_up_service', 'Услуга будильник / будильник'),
    ('minibar', 'Минибар'),
    ('flat_screen_tv', 'Телевизор с плоским экраном'),
    ('bath_or_shower', 'Ванна/душ'),
    ('Комоды', 'Комоды'),
    ('Мини кухня', 'Мини кухня'),
    ('Камин', 'Камин'),
    ('Закуски', 'Закуски'),
    ('2 комнаты', '2 комнаты'),
)


RATING_CHOICES = (
    ('Замечательно', 'Замечательно'),
    ('Отлично', 'Отлично'),
    ('Хорошо', 'Хорошо'),
    ('Неплохо', 'Неплохо'),
    ('Не оценено', 'Не оценено'),
)

STAR_CHOICES = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),
    (0, 'Без звезд'),
)
