import time

def time_it(fn, *args, repetitions= 1, **kwargs):
	"""This is a genralized function to call any function
	user specified number of times and return the average
	time taken for calls"""
	if repetitions < 0:
		raise ValueError("Repetitions should be positive number")
	if repetitions == 0:
		return 0
	
	start = time.perf_counter()
	for _ in range(repetitions):
		fn(*args, **kwargs)
	end = time.perf_counter()
	
	return (end - start)/repetitions

def squared_power_list(number,*args, start=0, end=5,**kwargs):
	"""Retruns list by raising number to power from start to end
	-> number**start to number**end. Default start is 0 and end is 5"""

	# Validations "if" block
	if type(number) != int:
		raise TypeError("Only integer type arguments are allowed")
	if start < 0 or end < 0:
		raise ValueError("Value of start or end can't be negative")
	if start > end:
		raise ValueError("Value of start should be less than end")
	if number > 10:
		raise ValueError("Value of number should be less than 10")
	if len(kwargs) > 0:
		raise TypeError("maximum 2 keyword/named arguments")
	if len(args) > 0:
		raise TypeError("takes maximum 1 positional arguments")
	
	# Return the list of number to the power of numbers from start to end
	return [number ** i for i in range(start, end)]


def polygon_area(length, *args, sides = 3, **kwargs):
	"""Retruns area of a regular polygon with number of sides between
	3 to 6 both inclusive"""

	# Validations
	if sides < 3 or sides > 6:
		raise ValueError("Number of sides should be between 3 and 6")
	if length <= 0:
		raise ValueError("Length should be positive number")
	if type(sides) != int:
		raise ValueError("Number of sides should be integer")
	if type(length) != int :
		raise TypeError("side length should be integer")
	if(len(kwargs) > 0):
		raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided")
	if(len(args) > 0):
		raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided")
	if not length:
		raise ValueError("Length should be provided")

	# Return area
	if sides == 3:
		return (length ** 2) * (3 ** 0.5) / 4
	elif sides == 4:    
		return length ** 2
	elif sides == 5:
		return 1.7204774005889674 * length ** 2
	elif sides == 6:
		return 2.598076211353316 * length ** 2
	
def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
	"""Converts temprature from celsius 'c' to fahrenheit 'f' or
	fahrenheit to celsius"""

	# Validations
	if type(temp) not in [int, float]:
		raise TypeError("Temperature should be integer or float")
	if type (temp_given_in) != str:
		raise TypeError("Character string expected")
	if temp_given_in.lower() not in ['c', 'f']:
		raise ValueError("Only f or c is allowed")
	if temp_given_in.lower() == 'c' and temp < -273.15:
		raise ValueError(".Temprature can't go below -273.15 celsius = 0 Kelvin")
	if temp_given_in.lower() == 'f' and temp < -459.67:
		raise ValueError(".Temprature can't go below -459.67 fahrenheit = 0 Kelvin")
	if len(kwargs) > 0:
		raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")
	if len(args) > 0:
		raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
	
	# Return the converted temprature
	if(temp_given_in.lower() == 'f'):
		return ((temp - 32) * 5)/9
	else:
		return (temp * 9/5) + 32
	
def speed_converter(speed, *args, dist='km', time='min', **kwargs):
	"""Converts speed from kmph (provided by user as input) to different units
	dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

	# Validations
	if len(kwargs) > 0:
		raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")
	if len(args) > 0:
		raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
	if type(speed) not in [int, float]:
		raise TypeError("Speed can be int or float type only")
	if type(dist) != str :
		raise TypeError("Charcater string expected for distance unit")
	if type(time) != str:
		raise TypeError("Charcater string expected")
	if speed < 0:
		raise ValueError("Speed can't be negative")
	if speed > 300000:
		raise ValueError("Speed can't be greater than speed of light")
	if time.lower() not in ['ms', 's', 'min', 'hr', 'day']:
		raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")
	if dist.lower() not in ['km', 'm', 'ft', 'yrd']:
		raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")
	
	
	# Return the converted speed
	final_speed = speed
	if dist.lower() == 'km':
		final_speed = final_speed
	elif dist.lower() == 'm':
		final_speed = final_speed * 1000
	elif dist.lower() == 'ft':
		final_speed = final_speed * 3280.84
	elif dist.lower() == 'yrd':
		final_speed = final_speed * 1093.61
	
	if time.lower() == 'ms':
		final_speed = final_speed / 3.6e+6
	elif time.lower() == 's':
		final_speed = final_speed / 3600.0
	elif time.lower() == 'min':
		final_speed = final_speed / 60.0
	elif time.lower() == 'hr':
		final_speed = final_speed
	elif time.lower() == 'day':
		final_speed = final_speed * 24
		
	return round(final_speed)
		
