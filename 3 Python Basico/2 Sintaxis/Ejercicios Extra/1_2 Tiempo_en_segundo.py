# Cree un programa que le pida un tiempo en segundos al usuario y 
# calcule si es menor o mayor a 10 minutos. 
# Si es menor, muestre cuantos segundos faltarían para llegar
# a 10 minutos. Si es mayor, muestre “Mayor”. 
# Si es exactamente igual, muestre “Igual”.
# Ejemplos:
# 1040 → Mayor
# 140 → 460
# 600 → Igual
# 599 → 1

#Solicitar tiempo en segundos
time_in_seconds = int(input("Ingrese tiempo en segundos: "))
#Calcular tiempo faltante 10 min = 600 seg
if time_in_seconds < 600:
    missing_seconds = 600 - time_in_seconds
    if missing_seconds == 1:
        message = f"Faltan {missing_seconds} segundo para llegar a 10 minutos"
    else:
        message = f"Faltan {missing_seconds} segundos0 para llegar a 10 minutos"
elif time_in_seconds == 600:
    message = "Igual"
else:
    message = "Mayor"

#Mostrar tiempo faltante o si es igual o mayor
print(message)