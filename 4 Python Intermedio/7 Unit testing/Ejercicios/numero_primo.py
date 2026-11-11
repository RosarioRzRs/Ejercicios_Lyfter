# Cree una función que acepte una lista de números y retorne 
# una lista con los números primos de la misma.
# [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
# Tip 1: Investigue la lógica matemática para 
# averiguar si un número es primo, y conviértala a código. 
# No busque el código, eso no ayudaría.
# Tip 2: Aquí hay que hacer varias cosas 
# (recorrer la lista, revisar si cada numero es primo, 
# y agregarlo a otra lista). Así que lo mejor es agregar
#  otra función para revisar si el numero es primo o no.

#Definir funcion y lista
def evaluate_prime_number(list_prime_number):
    if not isinstance(list_prime_number, list):
        raise ValueError("El parametro debe ser una Lista")
    
    if not all(isinstance(x, (int)) for x in list_prime_number):
        raise ValueError("Los elementos de la lista deben ser solo numeros enteros")
    
    new_list_prime_number = []
    for record in list_prime_number:
        sqrt_number = int(record ** (0.5))
        prime_number = 0
        for index in range (1, sqrt_number+1):
            mod_number = record % index
            if mod_number == 0:
               prime_number += 1
        if prime_number <= 1 and record != 1:
            new_list_prime_number.append(record)

    return new_list_prime_number

if __name__ == "__main__":
    # my_list_prime_number = [1, 4, 6, 7, 13, 9, 67]
    my_list_prime_number = 8
    # my_list_prime_number = "hola"
    # my_list_prime_number = [1, 4, 6, 7, 13, 9, "hola"]
    # my_list_prime_number = [1, 4, 6, 7, 13, 9.8]
    try:
        #Llamado de funcion e imprimir nueva lista
        message = evaluate_prime_number(my_list_prime_number)
        print(message)
    except ValueError as ex:
        print(ex)