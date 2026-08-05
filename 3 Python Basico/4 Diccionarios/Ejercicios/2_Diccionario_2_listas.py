# Cree un programa que cree un diccionario usando dos listas 
# del mismo tamaño, usando una para sus keys, y 
# la otra para sus values.
# Ejemplos:
# list_a = [’first_name’, ‘last_name’, ‘role’]
# list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]
# → {’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}

#Definicion de lista y diccionario
list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]
user_data = {}
#Crear Diccionario
for index in range(0, len(list_a)):
    user_data[list_a[index]] = list_b[index]
#Imprimir diccionario
message = user_data
print(message)