import csv

def save_list_of_students(file_path, data):
    # Abrimos el archivo en modo escritura ('w')
    # Usamos newline='' para que no se agreguen líneas en blanco entre registros
    if len(data) > 0:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
        #  try:
                # Obtenemos los nombres de las columnas con las llaves del primer registro
                headers = data[0].keys()
                # Inicializamos el escritor indicando el archivo destino y los encabezados
                writer = csv.DictWriter(file, fieldnames=headers)
                # Escribimos la primera fila en el documento con los títulos
                writer.writeheader()
                # Insertamos la lista completa de nuestras series
                writer.writerows(data)
                print("Archivo exportado con Exito")
    else:
         print("************* Archivo vacio, Registre un Estudiante para poder exportar *************")
         
  

def read_list_of_students(file_path):
    try:
        # Abrimos el archivo en modo lectura con soporte para utf-8
        with open(file_path, 'r', encoding='utf-8') as file:
            # DictReader convierte cada fila en un diccionario
            list_of_students =[]
            local_list_of_students = csv.DictReader(file)
            print("Archivo importado con Exito")
            for student in local_list_of_students:
                student['spanish_note'] = int(student['spanish_note'])
                student['english_note'] = int(student['english_note'])
                student['social_note'] = int(student['social_note'])
                student['science_note'] = int(student['science_note'])
                student['average_note'] = float(student['average_note'])
                list_of_students.append(student)
            return list_of_students
    except FileNotFoundError:
        print("Archivo no encontrado, Exporte primero el archivo")
            
