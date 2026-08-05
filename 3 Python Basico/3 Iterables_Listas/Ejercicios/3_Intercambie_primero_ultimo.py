# Cree un programa que intercambie el primer y ultimo elemento
# de una lista. Debe funcionar con listas de cualquier tamaño.
# Ejemplos:
# my_list = [4, 3, 6, 1, 7] → [7, 3, 6, 1, 4]

my_list = [15, 4, 3, 6, 1, 7, 10]
#Obtener posicion de la lista

pos_last_list = len(my_list)-1
#Imprimir lista original

message = my_list
print(message)

#Se borra valor de la ultima posicion de la lista y se guarda
#para posteriormente ingresarla en la posicion 0
deleted_last_item = my_list.pop(pos_last_list)
#Se inserta el ultimo valor de la lista en la poscion 0
my_list.insert(0, deleted_last_item)
#Se borra la posicion 1 y se guarda para 
#posteriormente agregar al final de la lista
deleted_first_item = my_list.pop(1)
#Se agrega un valor al final de la lista
my_list.append(deleted_first_item)
#Imprimir el nueva oren de la lista

message = my_list
print(message)