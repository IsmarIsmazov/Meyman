# Meyman
Meyman - это ваш надежный спутник в удивительном мире Кыргызстана. Наши услуги предназначены для путешественников, которые ищут идеальное место для отдыха и исследования этой прекрасной страны. Мы предоставляем следующие возможности:
- **Поиск отелей и санаториев: Вы сможете легко найти разнообразные варианты размещения, от роскошных отелей до уютных санаториев.**
- **Бронирование: Забронируйте свое проживание в несколько кликов и гарантированно зарезервируйте место, чтобы ваше путешествие прошло комфортно.**

Meyman делает ваше путешествие по Кыргызстану более удобным и захватывающим. Путешествуйте с нами и открывайте всю красоту этой уникальной страны.
## Преимущества сайта
- **Привлекательный дизайн**: Мы разработали лендинг с современным и привлекательным дизайном, который заинтересовывает с первого взгляда!
- **Краткость и четкость**: Мы предоставляем максимально простой и удобный сайт, чтобы пользователь мог легко ориентироваться и не утопать в лишней информации.
- **Простая работа с сайтом**: Удобная и интуитивная панель администратора, в которой есть все для приятной работы с клиентами!
****
## Запуск проекта
[![Python 3.11](https://img.shields.io/badge/Python-3.11-Green?style=for-the-badge&logo=Python)](https://www.python.org)
[![PostgreSQL 15](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=PostgreSQL)](https://www.postgresql.org/)
![Django](https://img.shields.io/badge/Django-4.2.3-092E20?style=for-the-badge&logo=Django)
![DRF](https://img.shields.io/badge/Django-RestFramework-0AC18E?style=for-the-badge&)
![Jazzmin](https://img.shields.io/badge/Jazzmin-2.6-A100FF?style=for-the-badge&)
![Pillow](https://img.shields.io/badge/Pillow-10-FF6550?style=for-the-badge&)
* Создание и активация виртуальной среды:
```shell
python -m venv venv
```
(Windows)
```shell
venv\Scripts\activate.bat
```
(Mac/Linux)
```shell
source venv/bin/activate
```

* Установка зависимостей:
```shell
pip install -r requirements.txt
```

* Создаем файл ".env" с полями:
```python
export SECRET_KEY=string
export DEBUG=on
export USER=str
export NAME=str
export PASSWORD=str
export HOST=localhost
export PORT=5432
```

* Запускаем и подключаем базу данных (PostgreSQL)


* Проводим миграции:
```shell
python manage.py makemigrations
```
```shell
python manage.py migrate
```

* Создаем аккаунт администратора:
```shell
python manage.py createsuperuser
```

* Запускаем сервер:
```shell
python manage.py runserver
```
***
## Карта проекта:
* Настройка и управление [Django](AroniaPharm/settings/base.py)
* Библиотека [Jazzmin](AroniaPharm/settings/jazzmin.py), для легкой и быстрой работы администратора
* Настройка [Cors](AroniaPharm/settings/local.py) для локальной работы с проектом
* Созданные [приложения](AroniaPharm/settings/development.py) и установленные библиотеки
* [Swagger и Redoc](AroniaPharm/settings/yasg.py) для работы Frontend и Android разработчиков
* В проекте были прописаны тесты к каждому приложению. Для запуска тестов используем python manage.py test apps.APP_NAME.tests.TEST_NAME"


***
Backend developers:
* [Ismar](https://t.me/Savadatsu)
* [Ulan](https://t.me/ekfybj)
* [Daniel](https://t.me/geeksdaniel)
* [Eldiar](https://t.me/elldiyar)
* [Syimyk](https://t.me/Abdykadyrov_S)
* [Islam](https://t.me/islaw_BT)
 