from django.contrib import admin
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, Rating


class HousingAdmin(admin.ModelAdmin):
    list_display = ['housing_name', 'location', 'price_per_night', 'housing_type', 'accommodation_type',
                    'bed_type', 'food_type']
    list_filter = ['housing_type']
    search_fields = ['housing_name']
    prepopulated_fields = {'slug': ('housing_name',)}


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating',)


@admin.register(Hotel)
class HotelAdmin(HousingAdmin):
    pass


@admin.register(Hostel)
class HostelAdmin(HousingAdmin):
    pass


@admin.register(Apartment)
class ApartmentAdmin(HousingAdmin):
    pass


@admin.register(GuestHouse)
class GuestHouseAdmin(HousingAdmin):
    pass


@admin.register(Sanatorium)
class SanatoriumAdmin(HousingAdmin):
    pass
