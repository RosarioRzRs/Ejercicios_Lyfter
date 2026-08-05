import csv

def read_list_of_games(file_path):
    local_list_of_games = []
    # Abrimos el archivo en modo lectura con soporte para utf-8
    with open(file_path, 'r', encoding='utf-8') as file:
        # DictReader convierte cada fila en un diccionario
        reader = csv.DictReader(file)

        for games in reader:
            local_list_of_games.append(games)

    return local_list_of_games


def look_for_classification(list_of_games, user_classification):
    count_classification = 0
    for index, games in enumerate(list_of_games):
        if games["classification ESRB"] == user_classification:
            print(f"Nombre: {games["name"]}")
            print(f"Genero: {games["gender"]}")
            print(f"Desarrollador: {games["developer"]}")
            print(f"Clasificacion: {games["classification ESRB"]}")
            count_classification += 1

    if count_classification == 0:
        print("Ningun videojuego encontrado con esta clasificacion")


def check_string(text):
    incorrect_text = text.isdigit()
    if incorrect_text:
        raise ValueError ("El dato ingresado no puede ser un numero, intente nuevamente")

    return True

def main():
    while True:
        try:
            user_classification = input("Ingrese una clasificacion ESRB: ")
            check_string(user_classification)
            break
        except ValueError as ex:
            print(ex)

    list_of_games = read_list_of_games('Ejercicios/Manejo de CSVs/Ejercicios/ejercicio_1.csv')
    look_for_classification(list_of_games, user_classification)


main()