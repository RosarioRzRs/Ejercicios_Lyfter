# Cree una función que reciba una lista de palabras y 
# un número n, y retorne una nueva lista con solo las 
# palabras que tengan más de n letras
# Ejemplo:
# Entrada:
# ["cielo","sol","maravilloso","día"]
# "Ingrese el numero de letras minimas en la palabra: "4
# Salida:["cielo", "maravilloso"]

def counter_of_letters (list, lenght):
    local_list = []
    for record in list:
        lenght_of_word = len(record)
        if lenght_of_word >= lenght:
            local_list.append(record)
    return local_list


#Solicitar informacion al usuario
user_list = input("Ingrese una lista separados por espacio: ")
user_lenght_of_word = int(input("Ingrese el numero de letras minimas en la palabra: "))
list = user_list.split()
#Imprimir 
message = counter_of_letters(list, user_lenght_of_word )
print(message)