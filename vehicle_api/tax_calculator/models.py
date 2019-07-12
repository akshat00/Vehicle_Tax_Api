from django.db import models

# Create your models here.
class Motorcycle(models.Model):
	vehicle_registration = models.CharField(max_length = 15)
	cc_begin = models.PositiveSmallIntegerField()
	cc_end = models.PositiveSmallIntegerField()
	_2070 = models.IntegerField()
	_2071 = models.IntegerField()
	_2072 = models.IntegerField()
	_2073 = models.IntegerField()
	_2074 = models.IntegerField()
	_2075 = models.IntegerField()

	def __str__(self):
		return str(self.cc_end)

class SmallVehicle(models.Model):
	vehicle_registration = models.CharField(max_length = 15)
	cc_begin = models.PositiveSmallIntegerField()
	cc_end = models.PositiveSmallIntegerField()
	_2070 = models.IntegerField()
	_2071 = models.IntegerField()
	_2072 = models.IntegerField()
	_2073 = models.IntegerField()
	_2074 = models.IntegerField()
	_2075 = models.IntegerField()

	def __str__(self):
		return str(self.cc_end)

class LargeVehicle(models.Model):
	vehicle_registration = models.CharField(max_length = 15)
	vehicle_type = models.CharField(max_length = 15)
	_2070 = models.IntegerField()
	_2071 = models.IntegerField()
	_2072 = models.IntegerField()
	_2073 = models.IntegerField()
	_2074 = models.IntegerField()
	_2075 = models.IntegerField()

	def __str__(self):
		return str(self.vehicle_type)
