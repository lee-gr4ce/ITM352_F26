def celsius_to_fahrenheit(temperature):
	return (temperature * 9 / 5) + 32

def fahrenheit_to_celsius(temperature):
	return (temperature - 32) * 5 / 9

def celsius_to_kelvin(temperature):
	return temperature + 273.15

def kelvin_to_celsius(temperature):
	return temperature - 273.15

def fahrenheit_to_kelvin(temperature):
	return celsius_to_kelvin(fahrenheit_to_celsius(temperature))

def kelvin_to_fahrenheit(temperature):
	return celsius_to_fahrenheit(kelvin_to_celsius(temperature))

def convert_temperature(temperature, conversion_function):
	return conversion_function(temperature)


temperature = float(input("Enter a temperature in Celsius: "))

print(f"{temperature} C = "
	  f"{convert_temperature(temperature, celsius_to_fahrenheit)} F")
print(f"{temperature} C = "
	  f"{convert_temperature(temperature, celsius_to_kelvin)} K")
