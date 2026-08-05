# Cree un programa con un numero secreto del 1 al 10. 
# El programa no debe cerrarse hasta que el usuario adivine el numero.
# Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random

# Genera un número del 1 al 10
random_number = random.randint(1, 10) 

#Solicitar numero secreto
secret_number = int (input("Adivine el numero secreto (1-10): "))

while secret_number != random_number :
    secret_number = int (input("Numero incorrecto, adivine nuevamente (1-10): "))

message = f"¡¡¡Felicidades, adivinsate el numero secreto --> {random_number} <-- !!!"
print (message)