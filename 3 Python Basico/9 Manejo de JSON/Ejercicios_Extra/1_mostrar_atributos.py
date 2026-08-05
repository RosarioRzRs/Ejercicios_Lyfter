
import json

def read_file_json(file_path):
    with open(file_path, mode="r", encoding="utf-8") as read_file:
       data_of_file = json.load(read_file)
       type(data_of_file)
    return data_of_file


def show_pokemon(list_pokemon):
    
    for index, pokemon in enumerate(list_pokemon):
        print(f"\n*****Pokemon No {index+1} ******\n")
        print(f"Nombre: { pokemon['name']}")
        print(f"Tipo: { pokemon['type']}")
        print(f"Nivel: { pokemon['level']}")
        print(f"Peso (Kg): { pokemon['weight_kg']}")
        print(f"Es brillante: { pokemon['is_shiny']}")
        print(f"Objeto equipado: { pokemon['held_item']}")
        for index_2 in range (4):
            print(f"Habilidad No. {index_2 + 1 }: { pokemon['skills'][index_2]}")
        print(f"Hp: { pokemon['stats']['hp']}")
        print(f"Ataque: { pokemon['stats']['attack']}")
        print(f"Defensa: { pokemon['stats']['defense']}")
        print(f"SP Ataque: { pokemon['stats']['sp_attack']}")
        print(f"SP Defensa: { pokemon['stats']['sp_defense']}")
        print(f"Velocidad: { pokemon['stats']['speed']}")       
   

def main():
    #Deserializacion desde un archivo Json
    data_from_json = read_file_json ("Ejercicios/Manejo de JSON/Ejercicios/Pokemones.json")
    #Mostrar pokemon
    show_pokemon(data_from_json)

    

#Lllamdado de funcion principal
main()