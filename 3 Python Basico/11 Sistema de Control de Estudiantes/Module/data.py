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
            list_of_students = csv.DictReader(file)
            print("====================== Informacion Importada del Sistema de Control de Estudiantes ======================\n")
            for student in list_of_students:
                # Accedemos a los datos usando los nombres de las columnas como claves
                show_student = f"-Nombre  completo: {student['name']}\n"
                show_student += f"-Sección: {student['section']}\n"
                show_student += "Notas:\n"
                show_student += f"-Español:  {student['spanish_note']}\n"
                show_student += f"-Inglés:   {student['english_note']}\n"
                show_student += f"-Sociales: {student['social_note']}\n"
                show_student += f"-Ciencias: {student['science_note']}\n"
                print(show_student)
    except FileNotFoundError:
        print("Archivo no encontrado, Exporte primero el archivo")
            
