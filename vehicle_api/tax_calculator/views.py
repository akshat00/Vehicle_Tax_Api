from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from bikram import samwat
from datetime import date, timedelta

from .models import Motorcycle, SmallVehicle, LargeVehicle
from .serializers import MotorcycleSerializer, SmallVehicleSerializer, LargeVehicleSerializer

def calculate(tax, valid_upto):
	dates = list((valid_upto.split('-')))

	temp = valid_upto
	valid_upto = samwat(int(dates[0]), int(dates[1]), int(dates[2]))
	current_date = samwat.from_ad(date.today())

	validity = valid_upto + timedelta(days = 365)
	validity = validity.as_tuple()
	validity = str(validity[0]) + '-' + str(validity[1]) + '-' + str(validity[2])

	number_of_days_left = current_date - valid_upto
	number_of_days_left = number_of_days_left.days

	if number_of_days_left <= 0:
		return 0, temp

	penalty_free_date = valid_upto.as_tuple()

	if(penalty_free_date[1] + 3 > 12):
		penalty_free_date = samwat(penalty_free_date[0]+1, 1, 1)
		penalty_free_date = penalty_free_date - timedelta(days = 1)

	else:
		penalty_free_date = samwat(penalty_free_date[0], penalty_free_date[1] + 3, penalty_free_date[2])

	if(penalty_free_date >= current_date):
		return tax, validity

	days_exceeded = current_date - penalty_free_date;
	days_exceeded = days_exceeded.days

	if days_exceeded <= 30:
		tax = tax + (0.05 * tax)

	elif days_exceeded <= 45:
		tax = tax + (0.1 * tax)

	else:
		current_date = current_date.as_tuple()

		if current_date[0] == int(dates[0]):
			tax = tax + (0.2 * tax)

		else:
			tax = tax + (0.32 * tax)

	return tax, validity


# Create your views here.

@api_view(['GET'])
def motorcycle_view(request, vehicle_registration_type, cubic_centimeter_capacity, valid_upto):
	queryset = Motorcycle.objects.all()
	serialize = MotorcycleSerializer(queryset, many = True)

	total_tax = 0

	while True:
		date = valid_upto.split('-')

		if int(date[0]) > 2075:
			year = '_2075'

		else:
			year = '_' + date[0]
		
		tax = 0

		for item in serialize.data:
			if(item['cc_end'] >= cubic_centimeter_capacity):
				tax = item[year]
				break

		if tax == 0:
			data = {'message':'invalid request'}
			return JsonResponse(data)

		calculated_amount = calculate(tax, valid_upto)

		if calculated_amount[0] == 0:
			break

		else:
			total_tax += calculated_amount[0]
			valid_upto = calculated_amount[1]

	data = {'tax':total_tax, 'validity':calculated_amount[1]}

	return JsonResponse(data)

@api_view(['GET'])
def smallvehicle_view(request, vehicle_registration_type, cubic_centimeter_capacity, valid_upto):
	queryset = SmallVehicle.objects.all()
	serialize = SmallVehicleSerializer(queryset, many = True)

	total_tax = 0

	while True:
		date = valid_upto.split('-')

		if int(date[0]) > 2075:
			year = '_2075'

		else:
			year = '_' + date[0]

		tax = 0

		for item in serialize.data:
			if(item['cc_end'] >= cubic_centimeter_capacity and item['vehicle_registration'] == vehicle_registration_type):
				tax = item[year]
				break

		if tax == 0:
			data = {'message':'invalid request'}
			return JsonResponse(data)

		calculated_amount = calculate(tax, valid_upto)
		
		if calculated_amount[0] == 0:
			break

		else:
			total_tax += calculated_amount[0]
			valid_upto = calculated_amount[1]

	data = {'tax':total_tax, 'validity':calculated_amount[1]}

	return JsonResponse(data)

@api_view(['GET'])
def largevehicle_view(request, vehicle_registration_type, vehicle_type, valid_upto):
	queryset = LargeVehicle.objects.all()
	serialize = LargeVehicleSerializer(queryset, many = True)

	total_tax = 0

	while True:
		date = valid_upto.split('-')

		if int(date[0]) > 2075:
			year = '_2075'

		else:
			year = '_' + date[0]

		tax = 0

		for item in serialize.data:
			if(item['vehicle_type'] == vehicle_type and item['vehicle_registration'] == vehicle_registration_type):
				tax = item[year]
				break

		if tax == 0:
			data = {'message':'invalid request'}
			return JsonResponse(data)

		calculated_amount = calculate(tax, valid_upto)
		
		if calculated_amount[0] == 0:
			break

		else:
			total_tax += calculated_amount[0]
			valid_upto = calculated_amount[1]

	data = {'tax':total_tax, 'validity':calculated_amount[1]}

	return JsonResponse(data)