# Cree un programa que reciba una lista de números y 
# calcule el promedio de los valores, 
# luego cree una nueva lista con solo los valores mayores al 
# promedio
# Ejemplo
# Entrada
# my_list = [10, 20, 30, 40, 50]
# Salida:
# "Promedio:" 30
# Nueva lista: [40, 50]
#Definir variables
my_list = []
new_list = []
average = 0
#Solicitar cantidad de notas y crear lista
len_my_list = int(input("Numero de Notas a ingresar: "))
message = f"Ingrese {len_my_list} valores: "
print (message)
for index in range (len_my_list):
    number = int(input(f"No {index + 1 } "))
    my_list.append(number)
    average = average + number
    if index == len_my_list-1:
        average = average/len_my_list
#Crear nueva lista con numero mayores al promedio
for record in my_list:
    if record > average:
        new_list.append(record)
#Imprimir promedio y nueva lista
message = f"Promedio: {average}"
print(message)
message = f"Nueva Lista {new_list}"
print(message)
