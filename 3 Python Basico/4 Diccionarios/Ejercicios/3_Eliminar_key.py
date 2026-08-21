# Cree un programa que use una lista para eliminar keys de un 
# diccionario.
# Ejemplos:
# list_of_keys = [’access_level’, ‘age’]
# employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’,
#              ‘access_level’: 5, ‘age’: 28}
# → {’name’: ‘John’, 'email’: ‘john@ecorp.com’}

#Definir lista y diccionario
list_of_keys = ["access_level", "age","address"]
list_for_deleted = []
employee = {
    "name" : "John",
    "email" : "john@ecorp.com",
    "access_level" : 5,
    "age" : 28,
}
# Se verifica que en el diccionario si exista los datos de la lista
# se crea una nueva lista
for record in list_of_keys:
    value_dictionary = employee.get(record)
    if value_dictionary == None:
        message = f"No existe '{record}' en el Diccionario"
        print(message)
    else:
        list_for_deleted.append(record)  
#Eliminar del diccionario de acuerdo al nuevo arreglo
for record in list_for_deleted:
    deleted_item = employee.pop(record)
#Imprimir lista
message = employee
print(message)