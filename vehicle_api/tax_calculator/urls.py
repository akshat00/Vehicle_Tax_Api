from django.urls import path, include
from .views import motorcycle_view, smallvehicle_view, largevehicle_view

urlpatterns = [
    path('motorcycle/<vehicle_registration_type>/<int:cubic_centimeter_capacity>/<valid_upto>', motorcycle_view, name = 'motorcycle'),
    path('smallvehicle/<vehicle_registration_type>/<int:cubic_centimeter_capacity>/<valid_upto>', smallvehicle_view, name = 'smallvehicle'),
    path('largevehicle/<vehicle_registration_type>/<vehicle_type>/<valid_upto>', largevehicle_view, name = 'largevehicle')
]