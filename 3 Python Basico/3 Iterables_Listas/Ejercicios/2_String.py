# Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
# Pista: investigue de que otras maneras se puede usar el range.
# Ejemplos:
# my_string = ‘Pizza con piña’ →
# a
# ñ
# i
# p

# n
# o
# c

# a
# z
# z
# i
# p
my_string = "Pizza con piña"
#Se obtiene longitud de la cadena
length = len(my_string)-1
#Se imprime caracter y se disminuye el indice
while length>=0:
    message = my_string[length]
    print(message)
    length -= 1
