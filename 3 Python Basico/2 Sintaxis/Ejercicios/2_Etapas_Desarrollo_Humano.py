# Cree un programa que le pida al usuario su 
# nombre, apellido, y edad,
# y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

###########Definir rango de edad
#Bebe: 0 a 2 años
#Niño: 2 a 10 años
#Preadolescente: 10 a 12 años
#Adolescente: 12 a 18 años
#Joven: 18 a 30 años
#Adulto: 30 a 60 años
#Adulto mayor: 60 años en adelaante

#Solicitar nombre, apellido y edad
name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int (input ("Ingrese su edad: "))
stage_list = ["Bebe", "Niño", "Preadolescente", "Adolescente", "Adulto Joven", "Adulto", "Adulto Mayor"]

if age <= 2:
    indice = 0
elif age > 2 and age <= 10:
     indice = 1
elif age > 10 and age <= 12:
     indice = 2     
elif age > 12 and age <= 20:
     indice = 3
elif age > 20 and age <= 40:
     indice = 4
elif age > 40 and age <= 65:
     indice = 5
else :
     indice = 6

message = f"{name} {last_name} de {age} años es clasificad@ como {stage_list[indice]} "
print (message)