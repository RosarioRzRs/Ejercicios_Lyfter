
import json

def read_file_json(file_path):
    with open(file_path, mode="r", encoding="utf-8") as read_file:
       data_of_file = json.load(read_file)
       type(data_of_file)
    return data_of_file


def write_file_json(file_path, data):
    with open(file_path, mode="w", encoding="utf-8") as write_file:
        json.dump(data, write_file, indent = 4)


def check_string(text):
    incorrect_text = text.isdigit()
    if incorrect_text:
        raise ValueError ("El dato ingresado no puede ser un numero, intente nuevamente")

    return True


def request_type_of_pokemon():
    while True:
        try:
            type_of_pokemon = input("Ingrese el tipo de pokemon desea buscar(agua, electrico, fuego, etc): ")
            check_string(type_of_pokemon)
            break
        except ValueError as ex:
            print(ex)

    return type_of_pokemon


def look_for_type_of_pokemon(list_of_pokemon, type_of_pokemon):
    pokemon_found = 0
    for pokemon in list_of_pokemon:
        if pokemon['type'] == type_of_pokemon:
            pokemon_found += 1
            if pokemon_found == 1:
                print("Los pokemos que existen de ese tipo son:")
            print(f"{pokemon['name']}")
    if pokemon_found == 0:
        print("Ningun pokemon del tipo ingresado")


def main():
    #Deserializacion desde un archivo Json
    data_from_json = read_file_json ("Ejercicios/Manejo de JSON/Ejercicios/Pokemones.json")
    #Obtener tipo de pokemon a buscar
    type_of_pokemon = request_type_of_pokemon()
    look_for_type_of_pokemon(data_from_json, type_of_pokemon)
  
 
#Llamado de funcion principal
main()