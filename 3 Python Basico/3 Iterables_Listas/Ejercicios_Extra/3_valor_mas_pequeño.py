# Cree un programa que muestre el valor más pequeño de una lista
# sin usar min().
# Use una variable para comparar uno a uno
#Definir varianles e inicializar
my_list = [9, 4, 7, 1, 5]
minimum_number = my_list[0]
#Buscar numero menor
for record in my_list:
    if record < minimum_number:
        minimum_number = record
#Imprimir mensaje
message = f"El menor valor es {minimum_number}"
print(message)

