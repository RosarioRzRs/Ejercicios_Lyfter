import csv

def save_list_of_games(file_path, data):
    # Abrimos el archivo en modo escritura ('w')
    # Usamos newline='' para que no se agreguen líneas en blanco entre registros
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        # Obtenemos los nombres de las columnas con las llaves del primer registro
        headers = data[0].keys()
        # Inicializamos el escritor indicando el archivo destino y los encabezados
        writer = csv.DictWriter(file, fieldnames=headers, delimiter= '\t')
        # Escribimos la primera fila en el documento con los títulos
        writer.writeheader()
        # Insertamos la lista completa de nuestras series
        writer.writerows(data)


def check_string(text):
    incorrect_text = text.isdigit()
    if incorrect_text:
        raise ValueError ("El dato ingresado no puede ser un numero, intente nuevamente")

    return True


def main():
    list_of_games = []
    while True:
        try:
            number_of_games = int(input("Cuantos juegos va a ingresar al archivo: "))
            break
        except ValueError:
            print("Valor inresado no es un numero, intente nuevamente")

    for index in range (0, number_of_games):
        message = f"Juego Numero {index + 1 } "
        print(message)
        while True:
            try:
                name = input ("Ingrese el nombre del juego: ")
                check_string(name)
                break
            except ValueError as ex:
                print(ex)
        while True:
            try:
                gender = input ("Ingrese el genero del juego: ")
                check_string(gender)
                break
            except ValueError as ex:
                print(ex)
        while True:
            try:
                developer = input ("Ingrese el nombre del Desarrollador : ")
                check_string(developer)
                break
            except ValueError as ex:
                print(ex)
        while True:
            try:
                classification = input ("Ingrese la clasificacion del juego: ")
                check_string(classification)
                break
            except ValueError as ex:
                print(ex)   
        
        list_of_games.append({"name" : name , "gender" : gender, "developer" : developer,"classification ESRB" : classification })
     

    save_list_of_games('Ejercicios/Manejo de CSVs/Ejercicios/ejercicio_2.csv', list_of_games)
    


main()
