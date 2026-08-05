# Cree una función que acepte un string con palabras separadas 
# por un guion y retorne un string igual pero ordenado alfabéticamente.
# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
# “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

#Definir funcion 
def sort_alphabetically (my_string):
    lenght_string = len(my_string) -1
    list_string = []
    word = ""
    #Separar
    for index, char in enumerate(my_string):
        if char != "-":
            word = word + char
        else:
            list_string.append(word)
            word = ""
        if index == lenght_string:
            list_string.append(word)
    #Ordenar
    list_string.sort()
    #Nueva string
    for index, record in enumerate(list_string):
        if index == 0:
            new_string = record
        else:
            new_string = new_string + "-" + record

    return new_string
        
   
my_string = "python-variable-funcion-computadora-monitor"
#imprimir nueva string
message = sort_alphabetically(my_string)
print(message)