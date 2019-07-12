from rest_framework import serializers
from .models import Motorcycle, SmallVehicle, LargeVehicle

class MotorcycleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Motorcycle
		fields = '__all__'

class SmallVehicleSerializer(serializers.ModelSerializer):
	class Meta:
		model = SmallVehicle
		fields = '__all__'

class LargeVehicleSerializer(serializers.ModelSerializer):
	class Meta:
		model = LargeVehicle
		fields = '__all__'