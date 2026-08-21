# Tabla de multiplicar personalizada
# Pida al usuario un número del 1 al 10
# Muestre su tabla de multiplicar del 1 al 12

#Solicitar un numero al usuario
number = int(input("Ingrese un número (1-10): "))

#Generar tabla e ,mostrar en pantalla
if number > 0 and number <= 10:
    for index in range (1, 13):
        result = number * index
        message = f"{number} x {index} = {result}"
        print(message)
else:
    message = "Numero no valido"
    print(message)