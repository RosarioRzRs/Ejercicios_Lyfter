
def selection():
    message = """
    1 Ingresar informacion de Estudiantes
    2 Mostrar informacion de Estudiantes
    3 Top 3 de los mejores Estudiantes
    4 Informacion de Estudiantes Reprobados
    5 Informacion de Promedio de los Estudiantes 
    6 Eliminar informacion de Estudiante
    7 Exportar CSV
    8 Importar CSV
    9 Cerrar Sistema de Control
    """
    print(message)

    while True:
        next_step = 0
        try:
            option_number = int (input("Ingrese una opcion: "))
            next_step = 1
        except ValueError:
            print("El valor ingresado no es un numero, ingrese nuevamente")

        while next_step == 1:
            try:
                if option_number > 9 or option_number < 1:
                    raise ValueError()
                else:
                    next_step = 2
                    break
            except ValueError:
                print("El valor ingresado no es una opcion valida, ingrese nuevamente")
                break

        if next_step == 2:
            break

    return option_number

    
if __name__ =='__main__':
    selection()