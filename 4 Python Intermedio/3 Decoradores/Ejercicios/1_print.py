# Cree un decorador que haga print de los 
# parámetros y retorno de la función que decore.


def print_parameters_and_returns(func):
    def wrapper(*args, **kwargs):
        print("******Parametros Originales*****")
        print(args)
        print(kwargs)
        print("-----Parametros solo Numeros-----")
        print(func(*args, **kwargs))
    return wrapper



@print_parameters_and_returns
def save_only_number(*args, **kwargs):
    list_of_number = []
    for record in args:
        if isinstance(record, (int, float)):
            list_of_number.append(record)
    for value in kwargs.values():
        if isinstance(value, (int, float)):
            list_of_number.append(value)
    return list_of_number




save_only_number("Hola", 3, 3.5, "Tarea", "Prueba", "Laura", kwargs_1 = 5, kwargs_2 = 8.5, kwargs_3 = "World" )