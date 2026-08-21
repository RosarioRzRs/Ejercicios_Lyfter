import random

def selection_operation():
    Selection = """Seleccione el tipo de Operaccion a realizar:
    1 Suma
    2 Resta
    3 Multiplicacion
    4 Division
    5 Borrar resultado"""
    print(Selection)
    local_other_number = 0
    while True:
        next_step = 0

        try:
            local_number_of_operation = int (input("Numero de Operaccion:"))
            next_step = 1
        except ValueError:
            print("El valor ingresado no es un numero, ingrese nuevamente")
            next_step = 0

        while next_step == 1:
            try:
                if local_number_of_operation >5 or local_number_of_operation < 1:
                    raise ValueError()
                    next_step = 0
                else:
                    next_step = 2
                    break
            except ValueError:
                next_step = 0
                print("El valor ingresado es una opcion invalida, ingrese nuevamente")
                break

        if next_step == 2:
            break
        
    while local_number_of_operation <= 4 and local_number_of_operation >= 1 :           
        try:
            local_other_number = int(input("Ingrese el otro numero: "))
            break
        except ValueError:
            print("El valor ingresado no es un numero, ingrese nuevamente")
            
    return local_number_of_operation, local_other_number


def calculator(number_selection_operation, number_1, number_2):
    match number_selection_operation:
        case 1:
                result_of_the_operation = addition(number_1, number_2)
        case 2:
                result_of_the_operation = subtraction(number_1, number_2)
        case 3:
                result_of_the_operation = multiplication(number_1, number_2)
        case 4:
                result_of_the_operation = division(number_1, number_2)
        case 5:
                result_of_the_operation = clear_result()

    return result_of_the_operation      


def addition(number_1, number_2):
    result_of_the_operation = number_1 + number_2
    message = f"Resultado de la operacion es:  {number_1} + {number_2} = {result_of_the_operation}"
    print(message)
    return result_of_the_operation


def subtraction(number_1, number_2):
    result_of_the_operation = number_1 - number_2
    message = f"Resultado de la operacion es:  {number_1} - {number_2} = {result_of_the_operation}"
    print(message)
    return result_of_the_operation


def multiplication(number_1, number_2):
    result_of_the_operation = number_1 * number_2
    message = f"Resultado de la operacion es:  {number_1} * {number_2} = {result_of_the_operation}"
    print(message)
    return result_of_the_operation


def division(number_1, number_2):
    try:
        result_of_the_operation = number_1 / number_2
        message = f"Resultado de la operacion es:  {number_1} / {number_2} = {result_of_the_operation}"
        print(message)
    except ZeroDivisionError as error:
        print(f"No se puede dividir entre 0")
        result_of_the_operation = number_1
    return result_of_the_operation


def clear_result():
    message = f"Borrando resultado...."
    print(message)
    result_of_the_operation = 0
    return result_of_the_operation


def main():
    actual_number = random.randint(1, 10) 

    while True:
        number_selection_operation, other_name = selection_operation()
        message = f"****Numero actual antes de la operacion: {actual_number} ****"
        print(message)
        result_of_the_operation = calculator(number_selection_operation, actual_number, other_name)
        actual_number = result_of_the_operation
        message = f"****Numero actual despues de la operacion: {actual_number} ****"
        print(message)

main()