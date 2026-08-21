
import json

def read_file_json(file_path):
    with open(file_path, mode="r", encoding="utf-8") as read_file:
       data_of_file = json.load(read_file)
       type(data_of_file)
    return data_of_file

def average_level(list_of_pokemon):
    dict_pokemon_type = {}
    for pokemon in list_of_pokemon:
        pokemon_type = pokemon['type']
        pokemon_level = pokemon['level']
        if pokemon_type not in dict_pokemon_type:
            dict_pokemon_type[pokemon_type]= []
        dict_pokemon_type[pokemon_type].append(pokemon_level)

    for type_pokemon, level_pokemon in dict_pokemon_type.items():
        average_level_by_type = 0
        for index in range(len(level_pokemon)):
            average_level_by_type = average_level_by_type + level_pokemon[index]
        average_level_by_type = average_level_by_type / len(level_pokemon)
        print (f"Tipo: {type_pokemon} → Promedio de nivel: {average_level_by_type}")

         
def main():
    #Deserializacion desde un archivo Json
    data_from_json = read_file_json ("Ejercicios/Manejo de JSON/Ejercicios/Pokemones.json")
    #Agrupar por tipo de pokemon
    average_level(data_from_json)
  
 
#Llamado de funcion principal
main()