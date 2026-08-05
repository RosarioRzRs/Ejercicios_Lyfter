# Dada n cantidad de notas de un estudiante, calcular:
# Cuantas notas tiene aprobadas (mayor a 70).
# Cuantas notas tiene desaprobadas (menor a 70).
# El promedio de todas.
# El promedio de las aprobadas.
# El promedio de las desaprobadas.

#Inicializar variables
grades_count = 1
number_approved_grades = 0
number_failing_grades = 0
average_approved_grades = 0
average_failing_grades = 0
average_total_grades = 0

total_grades = int(input("Ingrese el total de las notas: "))

while grades_count <= total_grades:
    message = f"Ingrese la nota numero {grades_count}: "
    actual_grade = int (input (message))

    if actual_grade < 70:
        number_failing_grades = number_failing_grades + 1
        average_failing_grades = average_failing_grades + actual_grade
    else:
        number_approved_grades = number_approved_grades + 1
        average_approved_grades = average_approved_grades + actual_grade
    
    average_total_grades = average_total_grades + (actual_grade / total_grades)
    grades_count = grades_count + 1

if number_failing_grades > 0:
    average_failing_grades = average_failing_grades / number_failing_grades
if number_approved_grades > 0:
    average_approved_grades = average_approved_grades / number_approved_grades

message = f"El estudiante tiene esta cantidad de notas aprobadas: {number_approved_grades}"
print(message)
message = f"Este es el promedio de notas aprobadas: {average_approved_grades}"
print(message)
message = f"El estudiante tiene esta cantidad de notas desaprobadas: {number_failing_grades}"
print(message)
message = f"Este es el promedio de notas desaprobadas: {average_failing_grades}"
print(message)
message = f"Este es el promedio total de notas: {average_total_grades}"
print(message)