# Cree una función que le dé la vuelta a un string 
# y lo retorne.
# Esto ya lo hicimos en iterables.
# “Hola mundo” → “odnum aloH”

#Definicion de funcion y string
def string(my_string):
    if not isinstance(my_string, str):
            raise ValueError("El parametro debe ser un string")
    length = len(my_string)-1
    message = ""
    for index in range(len(my_string)-1, -1, -1):
        message = message + my_string[index]

    return message

if __name__ == "__main__":
    my_string = "Hola mundo"
    # my_string = 2568
    try:
        message = string(my_string)
        print(message)
    except ValueError as ex:
         print(ex)
    #Llamado de funcion
    