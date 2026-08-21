# Cree un programa que cuente cuántas veces aparece un número
#  específico en una lista.
#  Pida al usuario una lista de números y 
# otro número a buscar

#Definir variables
user_list = []
count = 0
#Solicitar numeros para la lista
message = "Ingresa 10 numeros: "
print(message)
for index in range (10):
    number = int(input(f"{index +1}: "))
    user_list.append(number)
#Solicitar numero a buscar
search = int(input("Ingresa numero a buscar: "))
#Contar cuantas veces aparece el numero en la lista
for record in user_list:
    if search == record:
        count += 1
#Imprimir cuantas veces aparece el numero en la lista
if count > 1:
    message = f"El numero {search} aparece {count} veces"
elif count == 1:
    message = f"El numero {search} aparece {count} vez"
else:
    message = f"El numero {search} no aparece en la lista"
print(message)