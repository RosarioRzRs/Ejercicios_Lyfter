# Cree una función que reciba un string y retorne cuántas 
# vocales contiene
# Ejemplo:
# Entrada:
# "Hola mundo"
# Salida:
# 4

def counter_of_vowels(string):
    counter_vowels = 0
    lower_string = string.lower()
    for char in lower_string:
        if char == "a" or char == "e" or char =="i" or char =="o" or char =="u":
             counter_vowels += 1
    return counter_vowels

#Solicitar informacion al usiario
user_string = input("Ingrese  una string: ")
number_of_vowels = counter_of_vowels (user_string)
#Imprimir numero de vocales
print(number_of_vowels)