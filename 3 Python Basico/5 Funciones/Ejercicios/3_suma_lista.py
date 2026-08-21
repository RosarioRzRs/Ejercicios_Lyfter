# Cree una función que retorne la suma de todos los 
# números de una lista.
# La función va a tener un parámetro (la lista) y retornar 
# un número (la suma de todos sus elementos).
# [4, 6, 2, 29] → 41
#Definir funcion y lista
def add_number_of_list(list):
    sum_list = 0
    for record in list:
        sum_list = sum_list + record

    return sum_list


my_list = [4, 6, 2, 29]
#Llamar funcion, guardar informacion e imprimir
sum = add_number_of_list(my_list)
print(sum)