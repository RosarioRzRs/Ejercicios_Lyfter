#Cree un programa que le pida tres números al usuario y muestre el mayor.

#Definir variables
number_list = [0,0,0]

#Solicitar al usuario los 3 numeros
number_list[0] = int( input("Ingrese el primer numero: "))
number_list[1] = int( input("Ingrese el segundo numero: "))
number_list[2] = int( input("Ingrese el tercer numero: "))

major_number = number_list[0]

for index_list in number_list:
    if index_list > major_number:
        major_number = index_list
    
message = f"El numero mayor es: {major_number}"

print(message)