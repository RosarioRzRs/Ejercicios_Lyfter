# Convertidor de unidades de temperatura
# Pida al usuario ingresar una temperatura en Celsius
# Conviértala a Fahrenheit y Kelvin
# Muestre los tres valores

#Solivitar temperatura
temperature_celsius = float(input("Ingrese temperatura en Celsius: "))

#Conversion
temperature_fahrenheit = temperature_celsius * 1.8 +32
temperature_kelvin = temperature_celsius + 273.15

#Mostrar temperaturas en Fahrenheit y Kelvin
message = f"Fahrenheit: {temperature_fahrenheit}"
print(message)
message = f"Kelvin: {temperature_kelvin}"
print(message)