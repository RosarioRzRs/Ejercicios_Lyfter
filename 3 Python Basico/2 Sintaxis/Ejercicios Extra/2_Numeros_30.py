
# Cree un programa que pida 3 números al usuario. Si uno de esos números es 30,
# o si los 3 sumados dan 30, mostrar “Correcto”. 
# Sino, mostrar “incorrecto”.
# Ejemplos:
# 23, 30, 768 → Correcto (hay un 30)
# 10, 15, 5 → Correcto (10 + 15 + 5 = 30)
# 35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)

#Solicitar 3 numeros al usuario
number_1 = int(input("Ingrese Numero 1: "))
number_2 = int(input("Ingrese Numero 2: "))
number_3 = int(input("Ingrese Numero 3: "))

#Saber si hay un 30 o la sumatoria es 30
condition = number_1== 30 or number_2 == 30 or number_3 == 30 or (number_1+number_2+number_3)==30

if condition:
    message = "Correcto"
else:
    message = "Incorrecto"
#Mostrar mensaje
print(message)