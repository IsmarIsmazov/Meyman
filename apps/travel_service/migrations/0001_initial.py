# Generated by Django 4.2.3 on 2023-09-14 04:19

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Мерседес-бенц', 'Мерседес-бенц'), ('Лендровер', 'Лендровер'), ('БМВ', 'БМВ'), ('Вольво', 'Вольво'), ('Шевролед', 'Шевролед'), ('Фольксваген', 'Фольксваген'), ('Хонда', 'Хонда'), ('Ауди', 'Ауди'), ('Хендай', 'Хендай'), ('Форд', 'Форд'), ('Киа', 'Киа'), ('Лексус', 'Лексус'), ('Мицубиси', 'Мицубиси'), ('Рено', 'Рено'), ('Опель', 'Опель'), ('Субару', 'Субару'), ('Мазда', 'Мазда'), ('Порше', 'Порше'), ('Дэу', 'Дэу'), ('Лада', 'Лада'), ('Сузуки', 'Сузуки'), ('Инфинити', 'Инфинити'), ('Ссанг Йонг', 'Ссанг Йонг'), ('Ниссан', 'Ниссан'), ('Тойота', 'Тойота')], max_length=50, verbose_name='Марка трансфера')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('category', models.CharField(choices=[('Легковушка', 'Легковушка'), ('Минивэн', 'Минивэн'), ('Внедорожник', 'Внедорожник'), ('Автобус', 'Автобус'), ('Кроссовер', 'Кроссовер')], max_length=50, verbose_name='Категория')),
                ('body_type', models.CharField(choices=[('Седан', 'Седан'), ('Купе', 'Купе'), ('Хэтчбек', 'Хэтчбек'), ('Лифтбек', 'Лифтбек'), ('Фастбэк', 'Фастбэк'), ('Универсал', 'Универсал'), ('Кроссовер', 'Кроссовер'), ('Внедорожник', 'Внедорожник'), ('Легковой фургон', 'Легковой фургон'), ('Минивэн', 'Минивэн'), ('Компактвэн', 'Компактвэн'), ('Микровэн', 'Микровэн'), ('Кабриолет', 'Кабриолет'), ('Родстер', 'Родстер'), ('Тарга', 'Тарга'), ('Ландо', 'Ландо'), ('Лимузин', 'Лимузин')], max_length=50, verbose_name='Тип кузова')),
                ('transmission', models.CharField(choices=[('Механическая', 'Механическая'), ('Автоматическая', 'Автоматическая'), ('Другое', 'Другое')], max_length=50, verbose_name='Тип коробки передач')),
                ('steering', models.CharField(choices=[('Левый', 'Левый'), ('Правый', 'Правый')], max_length=50, verbose_name='Руль')),
                ('drive_type', models.CharField(choices=[('Передний', 'Передний'), ('Задний', 'Задний'), ('Полный', 'Полный')], max_length=50, verbose_name='Тип привода')),
                ('fuel_type', models.CharField(choices=[('Бензин', 'Бензин'), ('Бензин/Газ', 'Бензин/Газ'), ('Газ', 'Газ'), ('Дизель', 'Дизель'), ('Электрический', 'Электрический'), ('Другое', 'Другое')], max_length=50, verbose_name='Тип топлива')),
                ('color', models.CharField(choices=[('Серебристый', 'Серебристый'), ('Черный', 'Черный'), ('Белый', 'Белый'), ('Серый', 'Серый'), ('Бежевый', 'Бежевый'), ('Бирюзовый', 'Бирюзовый'), ('Бордовый', 'Бордовый'), ('Бронза', 'Бронза'), ('Хамелеон', 'Хамелеон'), ('Жёлтый', 'Жёлтый'), ('Зеленый', 'Зеленый'), ('Золотой', 'Золотой'), ('Коричневый', 'Коричневый'), ('Фиолетовый', 'Фиолетовый'), ('Синий', 'Синий'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Розовый', 'Розовый'), ('Сиреневый', 'Сиреневый'), ('Вишня', 'Вишня'), ('Баклажан', 'Баклажан'), ('Голубой', 'Голубой')], max_length=50, verbose_name='Цвет')),
                ('passenger', models.CharField(choices=[('2 passengers', '2 пассажира'), ('5 passengers', '5 пассажиров'), ('8 passengers', '8 пассажиров'), ('Другое', 'Другое')], max_length=50, verbose_name='Вместимость пассажиров')),
                ('condition', models.CharField(choices=[('Хорошее', 'Хорошее'), ('Идеальное', 'Идеальное'), ('Новое', 'Новое')], max_length=50, verbose_name='Состояние автомобиля')),
                ('fuel_consumption', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Расход топлива на 100км')),
                ('minimum_age', models.PositiveIntegerField(verbose_name='Минимальный возраст водителя')),
                ('passenger_sits', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20)], default=1, verbose_name='Пассажирских мест')),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1970), django.core.validators.MaxValueValidator(2025)], verbose_name='Год выпуска')),
                ('driving_experience', models.PositiveIntegerField(verbose_name='Минимальный стаж вождения для аренды')),
                ('amenities', multiselectfield.db.fields.MultiSelectField(choices=[('Кондиционер', 'Кондиционер'), ('Датчик парковки', 'Датчик парковки'), ('Подогрев сидений и руля', 'Подогрев сидений и руля'), ('Детское кресло', 'Детское кресло')], max_length=150, verbose_name='Внутренние удобства')),
                ('safety_equipment', multiselectfield.db.fields.MultiSelectField(choices=[('Наличие огнетушителя', 'Наличие огнетушителя'), ('Наличие аптечки', 'Наличие аптечки'), ('Наличие запасного колеса', 'Наличие запасного колеса'), ('Наличие подушка безопасности', 'Наличие подушка безопасности'), ('Наличие инструментов аварийной ситуации', 'Наличие инструментов аварийной ситуации'), ('Наличие авторегистратора', 'Наличие авторегистратора')], max_length=255, verbose_name='Наличие системы безопасности')),
                ('pickup_location', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Чуй', 'Чуй'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=100, verbose_name='Место получения')),
                ('return_location', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Чуй', 'Чуй'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=100, verbose_name='Место возврата')),
                ('check_in_time', models.TimeField(verbose_name='Время заезда')),
                ('check_out_time', models.TimeField(verbose_name='Время отъезда')),
                ('can_arrange_pickup_return', models.BooleanField(default=True, verbose_name='Договор о месте получения/возврата автомобиля')),
                ('driver_service', models.BooleanField(default=False, verbose_name='Услуга водителя')),
                ('operating_area', multiselectfield.db.fields.MultiSelectField(choices=[('Бишкек', 'Бишкек'), ('Чуй', 'Чуй'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен'), ('По всему КР', 'По всему КР')], max_length=100, verbose_name='Территории эксплуатации')),
                ('currency', models.CharField(choices=[('Сом (KGS)', 'Сом (KGS)'), ('Доллар (USD)', 'Доллар (USD)'), ('Евро (EUR)', 'Евро (EUR)')], max_length=25, verbose_name='Валюта')),
                ('rental_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма аренды (Сутки)')),
            ],
            options={
                'verbose_name': 'Трансфер',
                'verbose_name_plural': 'Трансферы',
            },
        ),
        migrations.CreateModel(
            name='TransferImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='transfers', verbose_name='Изображения Трансфера')),
            ],
            options={
                'verbose_name': 'Изображение трансфера',
                'verbose_name_plural': 'Изображения трансферов',
            },
        ),
        migrations.CreateModel(
            name='TransferReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_location', models.CharField(max_length=255, verbose_name='Место получения трансфера')),
                ('destination_location', models.CharField(max_length=255, verbose_name='Куда вы хотите поехать')),
                ('pickup_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 9, 14))], verbose_name='Дата получения трансфера')),
                ('return_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 9, 14))], verbose_name='Дата возврата трансфера')),
                ('pickup_time', models.TimeField(verbose_name='Время получения трансфера')),
                ('return_time', models.TimeField(verbose_name='Время возврата трансфера')),
                ('return_location', models.CharField(max_length=255, verbose_name='Место возврата трансфера')),
                ('different_pickup_places', models.BooleanField(default=False, verbose_name='Разные места получения')),
                ('with_driver', models.BooleanField(default=False, verbose_name='Трансфер с водителем')),
            ],
            options={
                'verbose_name': 'Бронь трансфера',
                'verbose_name_plural': 'Бронь Трансферов',
            },
        ),
        migrations.CreateModel(
            name='TransferReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=500, null=True, verbose_name='Комментарий')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('how_it_went', models.IntegerField(choices=[(10, 'Замечательно'), (9, 'Превосходно'), (8, 'Очень хорошо'), (7, 'Хорошо'), (6, 'Достаточно хорошо'), (5, 'Нормально'), (4, 'Неудовлетворительно'), (3, 'Плохо'), (2, 'Очень плохо'), (1, 'Ужасно')], verbose_name='Как все прошло')),
                ('comfortable_driving', models.IntegerField(choices=[(10, 'Замечательно'), (9, 'Превосходно'), (8, 'Очень хорошо'), (7, 'Хорошо'), (6, 'Достаточно хорошо'), (5, 'Нормально'), (4, 'Неудовлетворительно'), (3, 'Плохо'), (2, 'Очень плохо'), (1, 'Ужасно')], verbose_name='Комфорт вождения')),
                ('technical_condition', models.IntegerField(choices=[(10, 'Замечательно'), (9, 'Превосходно'), (8, 'Очень хорошо'), (7, 'Хорошо'), (6, 'Достаточно хорошо'), (5, 'Нормально'), (4, 'Неудовлетворительно'), (3, 'Плохо'), (2, 'Очень плохо'), (1, 'Ужасно')], verbose_name='Техническое состояние')),
                ('cleanliness_level', models.IntegerField(choices=[(10, 'Замечательно'), (9, 'Превосходно'), (8, 'Очень хорошо'), (7, 'Хорошо'), (6, 'Достаточно хорошо'), (5, 'Нормально'), (4, 'Неудовлетворительно'), (3, 'Плохо'), (2, 'Очень плохо'), (1, 'Ужасно')], verbose_name='Уровень чистоты')),
                ('price_quality_ratio', models.IntegerField(choices=[(10, 'Замечательно'), (9, 'Превосходно'), (8, 'Очень хорошо'), (7, 'Хорошо'), (6, 'Достаточно хорошо'), (5, 'Нормально'), (4, 'Неудовлетворительно'), (3, 'Плохо'), (2, 'Очень плохо'), (1, 'Ужасно')], verbose_name='Соотношение цены и качества')),
                ('safety_level', models.IntegerField(choices=[(10, 'Замечательно'), (9, 'Превосходно'), (8, 'Очень хорошо'), (7, 'Хорошо'), (6, 'Достаточно хорошо'), (5, 'Нормально'), (4, 'Неудовлетворительно'), (3, 'Плохо'), (2, 'Очень плохо'), (1, 'Ужасно')], verbose_name='Уровень безопасности')),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='travel_service.transfer', verbose_name='Название трансфера')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
