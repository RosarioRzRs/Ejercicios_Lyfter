# Cree un decorador que haga print de los 
# parámetros y retorno de la función que decore.


def print_parameters_and_returns(func):
    def wrapper(value):
        print("******Lista Original*****")
        for record in value:
            print(record)
        print("-----Lista de solo Numeros-----")
        for record in func(value):
            print(record)
    return wrapper



@print_parameters_and_returns
def create_list_of_number(list_of_number):
    new_list = []
    for record in list_of_number:
        if isinstance(record, (int, float)):
            new_list.append(record)
    return new_list



my_list = ["Hola", 3, 3.5, "Tarea", "Prueba", "Laura"]
create_list_of_number(my_list)