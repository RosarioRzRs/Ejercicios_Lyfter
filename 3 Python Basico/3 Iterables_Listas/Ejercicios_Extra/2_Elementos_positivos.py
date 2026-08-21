# Cree un programa que verifique si todos los elementos 
# de una lista son positivos
# Restricciones:
# No use funciones como all()


my_list = [3, 6, 0, -2, 4]
message = my_list
print(my_list)
#Evalua una condicion, detiene la busqueda en cuanto cumple si es menor o igual a 0
negative_cero_number = False
for record in my_list:
    if record <= 0:
        negative_cero_number = True
        break
#Imprimir mensaje
if negative_cero_number:
    message = "Hay al menos un número negativo o cero"
else:
    message = "Todos son numeros positivos"
print(message)