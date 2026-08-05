
import json

def read_file_json(file_path):
    with open(file_path, mode="r", encoding="utf-8") as read_file:
       data_of_file = json.load(read_file)
       type(data_of_file)
    return data_of_file


def show_pokemon(list_pokemon):
    for index, pokemon in enumerate(list_pokemon):
        print(f"Nombre: { pokemon['name']}")
        print(f"Ataque: { pokemon['stats']['attack']}")
        print(f"Defensa: { pokemon['stats']['defense']}")
        print(f"Velocidad: { pokemon['stats']['speed']}")  
        print("\n")     
   

def main():
    #Deserializacion desde un archivo Json
    data_from_json = read_file_json ("Ejercicios/Manejo de JSON/Ejercicios/Pokemones.json")
    #Mostrar pokemon
    show_pokemon(data_from_json)

    

#Lllamdado de funcion principal
main()