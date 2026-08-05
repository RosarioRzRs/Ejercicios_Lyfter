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


def look_for_developer(list_of_games, user_developer):
    print(f"Videojuegos desarrollados por {user_developer}:")
    count_developer = 0
    for index, games in enumerate(list_of_games):
        if games["developer"] == user_developer:
            message = f"-{games["name"]} (Clasificación: {games["classification ESRB"]}, Género: {games["gender"]})"
            print(message)
            count_developer += 1
    if count_developer == 0:
        print("Ningun videojuegos encontrado por este Desarrollador")


def check_string(text):
    incorrect_text = text.isdigit()
    if incorrect_text:
        raise ValueError ("El dato ingresado no puede ser un numero, intente nuevamente")

    return True

def main():
    while True:
        try:
            user_developer = input("Ingrese un desarrollador: ")
            check_string(user_developer)
            break
        except ValueError as ex:
            print(ex)

    list_of_games = read_list_of_games('Ejercicios/Manejo de CSVs/Ejercicios/ejercicio_1.csv')
    look_for_developer(list_of_games, user_developer)


main()