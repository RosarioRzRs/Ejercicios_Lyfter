# Cree un programa que le pida al usuario ingresar 5 palabras. 
# Luego muestre una nueva lista con solo aquellas palabras 
# que tengan más de 4 letras


new_list = []
#Solicitar lista
message = "Ingrese 5 palabras: "
print(message)
#Ingresar las palabra y crear lista
for index in range (5):
    word = input()
    if len(word)>4:
        new_list.append(word)
#Mostrar nueva lista
message = new_list
print(message)


