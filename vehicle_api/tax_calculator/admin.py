from django.contrib import admin
from .models import Motorcycle, SmallVehicle, LargeVehicle

# Register your models here.
admin.site.register(Motorcycle)
admin.site.register(SmallVehicle)
admin.site.register(LargeVehicle)