# Cree un decorador que se encargue de revisar si todos los 
# parámetros de la función que decore son números, 
# y arroje una excepción de no ser así.

def only_numbers(func):
    def wrapper(*args):
        for record in args:
            if not isinstance(record, (int, float)):
                raise ValueError("Hay por lo menos un elemento que no es un numero")

        return func(*args)
     
    return wrapper



@only_numbers
def addition_list_of_number(*args):
    result = 0
    for record in args:
        result += record
    print(f"La sumatoria total es: {result}")

try:
    addition_list_of_number( 3, 3.5, 8, 10 ,101)
    # addition_list_of_number("Hola", 3, 3.5, "Tarea", "Prueba", "Laura")
except ValueError as ex:
    print(ex)
