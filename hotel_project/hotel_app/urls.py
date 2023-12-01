from django.urls import path
from .views import hotel_info

urlpatterns = [
    path('hotel-info/', hotel_info, name='hotel_info'),
]
