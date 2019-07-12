# VEHICLE TAX CALCULATOR
The api is powered by Django and can be used to calculate the tax for various types of vehicles in Nepal.

# End Points:
### For vehicle type 'motorcycle':
`GET motorcycle/<str:vehicle_registration_type>/<int:cubic_centimeter_capacity>/<str:valid_upto>`

#####  Values For Above Arguments:
- <vehicle_registration_type> : ['public', 'private']
- <cubic_centimeter_capacity> : Applicable value for the automobile.
- <valid_upto> : The date upto which the tax was last paid. The date should of format 'yyyy-mm-dd' (Note: Use dashes "-" to seperate the days, months, and years)

### For vehicle types 'car', 'jeep', 'van', 'micro-bus':
`GET smallvehicle/<vehicle_registration_type>/<int:cubic_centimeter_capacity>/<valid_upto>`

##### Values For Above Arguments:
- <vehicle_registration_type> : ['public', 'private']
- <cubic_centimeter_capacity> : Applicable value for the automobile.
- <valid_upto> : The date upto which the tax was last paid. The date should of format 'yyyy-mm-dd' (Note: Use dashes "-" to seperate the days, months, and years)

### For vehicle types 'dozer', 'excavator', 'loader', 'roller', 'tipper', 'crane', 'mini-tipper', 'mini-truck', 'mini-bus', 'truck', 'bus':
`GET largevehicle/<vehicle_registration_type>/<vehicle_type>/<valid_upto>`

##### Values For Above Arguments:
- <vehicle_registration_type> : ['public', 'private']
- <vehicle_type> : ['dozer', 'excavator', 'loader', 'roller', 'tipper', 'crane', 'mini_tipper', 'mini_truck', 'mini_bus', 'truck', 'bus']
- <valid_upto> : The date upto which the tax was last paid. The date should of format 'yyyy-mm-dd' (Note: Use dashes "-" to seperate the days, months, and years)

### JSON Return Format:
```json
{
    "tax": 4400, 
    "validity": "2077-3-14"
}
```

### Note :
The above end points can be run locally by running the Django development server and then using the below address on your preferred browser with the relevant end-points:
```sh
127.0.0.1:8000
```

# EXAMPLE CODE TO ACCESS API
```python
import requests
import json

vehicle_registration = 'public'
vehicle_type = 'motorcycle'
cubic_centimeter_capacity = '200'
valid_upto = '2076-03-15'

url = 'http://127.0.0.1:8000'

url = url + '/' + vehicle_type + '/' + vehicle_registration + '/' + cubic_centimeter_capacity + '/' + valid_upto

data = requests.get(url)
data = data.text

data = json.loads(data)

print('Tax Amount Due : ', data['tax'])
print('Valid Upto : ', data['validity'])
```

```python
import requests
import json

vehicle_registration = 'private'
vehicle_type = 'smallvehicle'
cubic_centimeter_capacity = '2500'
valid_upto = '2075-03-15'

url = 'http://127.0.0.1:8000'

url = url + '/' + vehicle_type + '/' + vehicle_registration + '/' + cubic_centimeter_capacity + '/' + valid_upto

data = requests.get(url)
data = data.text

data = json.loads(data)

print('Tax Amount Due : ', data['tax'])
print('Valid Upto : ', data['validity'])
```

