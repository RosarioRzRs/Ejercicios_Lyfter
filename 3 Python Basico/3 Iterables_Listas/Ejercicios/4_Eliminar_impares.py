# Cree un programa que elimine todos los números impares 
# de una lista.
# Ejemplos:
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Inicializar variable
index = 0
len_my_list = len (my_list)
#Mostrar lista original
message = my_list
print(message)    
#Buscar numero impar y borrar. Si es par, incrementa indice
while index < len_my_list:
    record = my_list[index]
    if record % 2 == 1:
        deleted_item = my_list.pop(index)
        len_my_list = len (my_list)
    else:
        index += 1
#Mostrar nueva lista
message = my_list
print(message)
