# Cree una función que le dé la vuelta a un string 
# y lo retorne.
# Esto ya lo hicimos en iterables.
# “Hola mundo” → “odnum aloH”

#Definicion de funcion y string
def string(my_string):
    length = len(my_string)-1
    message = ""
    for index in range(len(my_string)-1, -1, -1):
        message = message + my_string[index]

    return message


my_string = "Hola mundo"
message = string(my_string)
#Llamado de funcion
print(message)