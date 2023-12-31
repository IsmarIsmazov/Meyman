from _decimal import Decimal

import requests
from rest_framework.exceptions import ValidationError

from apps.currency_conversion.openexchangerates import OpenExchangeRatesClient, OpenExchangeRatesClientException


def get_average_rating(self, obj):
    from apps.travel.models import HousingReview
    reviews = HousingReview.objects.filter(housing=obj)
    if reviews:
        total_rating = sum([
            (review.staff_rating +
             review.comfort_rating +
             review.cleanliness_rating +
             review.value_for_money_rating +
             review.food_rating +
             review.location_rating) / 6
            for review in reviews
        ])
        average_rating = total_rating / len(reviews)
        return round(average_rating, 1)
    return 0


def compress_image(self):
    from PIL import Image
    if self.image:
        img = Image.open(self.image.path)
        if img != 'null' or img != "None":
            img = img.convert('RGB')
            img.thumbnail((800, 800))
            img.save(self.image.path, 'JPEG', quality=90)
        else:
            pass
    else:
        pass


def get_room_name(self, obj):
    try:
        room = obj.housing.rooms.first()
        if room:
            return room.room_name
    except Exception as e:
        pass
    return None


def validate_beds(single_bed, double_bed, queen_bed, king_bed, sofa_bed):
    total_beds = (single_bed or 0) + (double_bed or 0) + (queen_bed or 0) + (king_bed or 0) + (sofa_bed or 0)
    if total_beds > 3:
        raise ValidationError("Общее количество кроватей не может превышать три.")


def validata_people(adults, children):
    total_people = (adults or 0) + (children or 0)
    if total_people > 6:
        raise ValidationError("Количество гостей н может быть больше шести")
    elif total_people < 1:
        raise ValidationError("Количество гостей не может быть равен 0")


def get_cheapest_room_price(self, obj):
    cheapest_price = None
    rooms = obj.rooms.all()
    for room in rooms:
        if cheapest_price is None or room.price_per_night < cheapest_price:
            cheapest_price = room.price_per_night
    return cheapest_price


def get_price_per_night_convertede(self, obj):
    target_currency = self.context.get('currency', 'USD')
    base_currency = 'USD'
    api_key = 'fa696137fbdd4a48b672f5a73c6a1818'
    client = OpenExchangeRatesClient(api_key)
    try:
        exchange_rates = client.latest(base=base_currency)
        if target_currency in exchange_rates['rates']:
            exchange_rate = exchange_rates['rates'][target_currency]
            return obj.price_per_night * Decimal(exchange_rate)
    except (OpenExchangeRatesClientException, requests.exceptions.RequestException):
        pass
    return obj.price_per_night


def get_cheapest_room_price_for_favorite(self, obj):
    cheapest_room = obj.housing.rooms.order_by('price_per_night').first()
    return cheapest_room.price_per_night if cheapest_room else None


def get_housing_image(self, obj):
    first_image = obj.housing_images.first()
    if first_image:
        return first_image.image.url
    else:
        return None


def get_housing_image_for_favorite(self, obj):
    housing_images = obj.housing.housing_images.all()
    if housing_images:
        return [image.image.url for image in housing_images]
    else:
        return None
