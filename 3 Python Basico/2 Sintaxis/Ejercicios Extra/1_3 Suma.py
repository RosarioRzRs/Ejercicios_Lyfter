# Cree un programa que le pida un numero al usuario, y 
# realice una suma de cada numero del 1 hasta ese número ingresado. 
# Luego muestre el resultado de la suma.
# 5 → 15 (1 + 2 + 3 + 4 + 5)
# 3 → 6 (1 + 2 + 3)
# 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

#Solicitar un numero al usuario
number = int(input("Ingrese un numero: "))
add_number = 0
#Ciclo para sumar hasta el numero ingresado
for index in range( 1, number + 1 ):
    add_number = add_number + index
    
#Mostrar resultado de la suma
message = f"El resultado de la suma es: {add_number}"
print(message)