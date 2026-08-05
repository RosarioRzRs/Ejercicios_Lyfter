# Cree un programa que le pida al usuario 10 números,
# y al final le muestre todos los números que ingresó, 
# seguido del numero ingresado más alto.
# Ejemplos:
# 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 →
# [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

#Inicializar lista
my_list = [ ]
#Solicitar numeros
message = "Ingrese 10 numeros"
print(message)

for index in range (10):
    number = int(input(f"{index+1}: "))
    my_list.append(number)
    if index == 0:
        major_number = number
    elif number > major_number:
        major_number = number

#Mostrar los 10 numeros ingresados y el numeor mas alto
message = f"{my_list}. El mas alto fue {major_number}"
print(message)
