import csv

def read_list_of_games(file_path):
    # Abrimos el archivo en modo lectura con soporte para utf-8
    with open(file_path, 'r', encoding='utf-8') as file:
        # DictReader convierte cada fila en un diccionario
        reader = csv.DictReader(file)

        for index, games in enumerate(reader):
            # Accedemos a los datos usando los nombres de las columnas como claves
            print(f"Juego {index + 1}" )
            print(f"Nombre: {games['name']}")
            print(f"Genero: {games['gender']}")
            print(f"Desarrollador: {games['developer']}")
            print(f"Clasificacion: {games['classification ESRB']}")
            

read_list_of_games('Ejercicios/Manejo de CSVs/Ejercicios/ejercicio_1.csv')
