# Experimente con el concepto de scope:
# Intente acceder a una variable definida dentro de una 
# función desde afuera.
# Intente acceder a una variable global 
# desde una función y cambiar su valor.


def function_1():
    my_local_variable = 100
    my_global_variable = 400
    return my_global_variable


my_global_variable = 200


function_1()
print(my_global_variable)
print(my_local_variable)

