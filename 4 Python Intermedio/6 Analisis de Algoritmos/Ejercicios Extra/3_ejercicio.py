# Analice la siguiente función:

def print_all_pairs(my_dict):
    for key1 in my_dict:  #  O(n)
        for key2 in my_dict:  # O(n^2)
            print(f"{key1}-{key2}")   # O(1)



# Preguntas:
# ¿Cuál es la complejidad temporal?
#    O(n^2)
# ¿Cuanto dura si hay 1 millón de claves?
# si se tiene 1 millon, entonces el total seria
#  1,000,000,000,000 de datos. investigando en la terminal se pueden  imprimir en promedio
#    100,000 por segundo.  asi que si se divide se tardaria en 
#  imprimir  10,000,000 segundos. Que convirtiendo en dias seria proximadamente
#  115 dias