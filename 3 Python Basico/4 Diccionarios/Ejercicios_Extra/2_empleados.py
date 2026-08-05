# Agrupar empleados por departamento
# Dada una lista de empleados donde cada uno tiene
# nombre, correo y departamento, 
# cree un diccionario que agrupe los empleados por su departamento:

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
department = {}

# department = {
# 'Ventas': [
#      {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
#      {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"}
#             ] ,
# 'TI' : [
#      {"name": "Ana", "email": "ana@empresa.com", "department": "TI"}
#         ],
# 'RRHH' : [
#     {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"}
#     ]
# }

#Crear diccionario, si ya existe la key, agregar info a esa lista
for record in employees:
    department_of_employee = record['department']
    department_of_directinary = department.get(department_of_employee)
    if department_of_directinary == None:
        department[department_of_employee] = [record]
    else:
        department[department_of_employee].append(record)
#Imprimir diccionario
message = department       
print(message)