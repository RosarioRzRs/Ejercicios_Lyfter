# Cree un programa que permita agregar un Pokémon 
# nuevo al archivo de la lección de Manejo de JSON.
# Debe leer el archivo para importar los Pokémones 
# existentes.
# Luego debe pedir la información del Pokémon a agregar.
# Finalmente debe guardar el nuevo Pokémon en el archivo.

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


def capture_new_pokemon():
    new_pokemon = {
      'name': '',
      'type':'',
      'level':0,
      'weight_kg':0.0,
      'is_shiny':False,
      'held_item':None,
      'skills':[
         "",
         "",
         "",
         ""
      ],
      'stats':{
         'hp':0,
         'attack':0,
         'defense':0,
         'sp_attack':0,
         'sp_defense':0,
         'speed':0
      },
   }
    
    print("Ingrese informacion del Pokemon: ")

    while True:
        try:
            new_pokemon['name'] = input("Nombre: ")
            check_string(new_pokemon['name'])
            break
        except ValueError as ex:
            print(ex)

    while True:
        try:
            new_pokemon['type'] = input("Tipo: ")
            check_string(new_pokemon['type'])
            break
        except ValueError as ex:
            print(ex)

    while True:
        try:
            new_pokemon['level'] = int(input("Nivel: "))
            break
        except ValueError:
            print("Valor ingresado no es un numero, intente nuevamente")       

    while True:
        try:
            new_pokemon['weight_kg'] = float(input("Peso (Kg): "))
            break
        except ValueError:
            print("Valor ingresado no es un numero, intente nuevamente")       

    is_shiny = input("Es brillante (si/no): ").strip().lower()
    new_pokemon['is_shiny'] = is_shiny in ['si', 's', 'true', 1]
    
    held_item = input("Objeto equipado: ").strip()
    new_pokemon['held_item'] = held_item if held_item else None

    for index in range (4):
        while True:
            try:
                new_pokemon['skills'][index] = input(f"Habilidad No. {index +1}: ")
                check_string (new_pokemon['skills'][index])
                break
            except ValueError as ex:
                print(ex)

    while True:
        try:
            new_pokemon['stats']['hp']= int(input("HP: "))
            break
        except ValueError:
            print("Valor ingresado no es un numero, intente nuevamente")       

    while True:   
        try:             
            new_pokemon['stats']['attack']= int(input("Ataque: "))
            break
        except ValueError:
                    print("Valor ingresado no es un numero, intente nuevamente") 

    while True:
        try:
            new_pokemon['stats']['defense']= int(input("Defensa: "))
            break
        except ValueError:
            print("Valor ingresado no es un numero, intente nuevamente") 

    while True:
        try:
            new_pokemon['stats']['sp_attack']= int(input("SP Ataque: "))
            break
        except ValueError:
            print("Valor ingresado no es un numero, intente nuevamente") 

    while True:
        try:
            new_pokemon['stats']['sp_defense']= int(input("SP Defensa: "))
            break
        except ValueError:
            print("Valor ingresado no es un numero, intente nuevamente") 

    while True:
        try:
            new_pokemon['stats']['speed']= int(input("Velocidad: "))
            break
        except ValueError:
            print("Valor ingresado no es un numero, intente nuevamente") 

    return new_pokemon


def main():
    #Deserializacion desde un archivo Json
    data_from_json = read_file_json ("Ejercicios/Manejo de JSON/Ejercicios/Pokemones.json")
    #Obtener nuevos datos del nuevo pokemon
    user_new_pokemon = capture_new_pokemon()
    #Agregar nuevos datos a la lista
    data_from_json.append(user_new_pokemon)
    #Serializacion al archivo Json
    write_file_json("Ejercicios/Manejo de JSON/Ejercicios/Pokemones.json", data_from_json )

#Lllamdado de funcion principal
main()