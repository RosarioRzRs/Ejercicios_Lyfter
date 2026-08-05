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


def count_of_gender(list_of_games):
    dictionary_of_gender_of_games = {}
    for games in list_of_games:
        gender_game = games["gender"]
        keys_of_directinary = dictionary_of_gender_of_games.get(gender_game)
        if keys_of_directinary == None:
            dictionary_of_gender_of_games[gender_game] = 1
        else:
            dictionary_of_gender_of_games[gender_game] += 1

    message = "Géneros encontrados: "
    print(message)
    for gender, counter in dictionary_of_gender_of_games.items():
        message = f"{gender}: {counter}"
        print(message)

def main():
    list_of_games = read_list_of_games('Ejercicios/Manejo de CSVs/Ejercicios/ejercicio_1.csv')
    count_of_gender(list_of_games)


main()