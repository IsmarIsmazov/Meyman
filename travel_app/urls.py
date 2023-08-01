from django.contrib import admin
from django.urls import path, include
from .settings.yasg import urlpatterns_swagger as doc_urls
from apps.travel.urls import router as travel_router
from apps.news.urls import router as news_router
from apps.travel_service.urls import router as travel_service_router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.registry.extend(travel_router.registry)
router.registry.extend(news_router.registry)
router.registry.extend(travel_service_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/travel/', include('apps.travel.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/news/', include('apps.news.urls')),
    path('api/weather/', include('apps.weather_forecast.urls')),
    path('api/travel_sevice/', include('apps.travel_service.urls')),
    path('api/currency_conversion', include('apps.currency_conversion.urls')),
    path('api/advertising', include('apps.advertising.urls')),
    path('api/review/', include('apps.review.urls')),
]

urlpatterns += doc_urls