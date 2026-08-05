# Cree una función que reciba un texto y un carácter, y 
# retorne cuántas veces aparece ese carácter en el texto
# Ejemplo:
# Entrada:
# "programacion"
# "Ingrese el carácter que desea buscar:"
# "o"
# Salida:
# "Se a encontrado 2 veces el carácter"

def receive_text_and_character (text, character):
    counter_of_character = 0
    for char in text:
        if char == character:
            counter_of_character += 1
    if counter_of_character > 1:
        message = f"Se a encontrado {counter_of_character } veces el carácter"
    else:
        message = f"Se a encontrado {counter_of_character } vez el carácter"
    return message

#Solicitar informacion al usuario
user_text = input("Ingrese un texto: ")
user_character = input("Ingrese el carácter que desea buscar: ")
#Imprimir 
message = receive_text_and_character(user_text, user_character)
print(message)