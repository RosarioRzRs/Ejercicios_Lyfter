import csv

class Student():
     def __init__(self, student_file):
            self.name = student_file['name']
            self.section = student_file['section']
            self.spanish_note = student_file['spanish_note']
            self.english_note = student_file['english_note']
            self.social_note = student_file['social_note']
            self.science_note = student_file['science_note']
            self.average_note = student_file['average_note']
    
          

def save_list_of_students(file_path, data):
    # Abrimos el archivo en modo escritura ('w')
    # Usamos newline='' para que no se agreguen líneas en blanco entre registros
    if len(data) > 0:
        list_of_students = []
        for student in data:
             dict_student = {
                  'name':student.name,
                  'section' : student.section,
                  'spanish_note' : student.spanish_note,
                  'english_note' : student.english_note,
                  'social_note' : student.social_note,
                  'science_note' : student.science_note,
                  'average_note' : student.average_note,
             }
             list_of_students.append(dict_student)

        with open(file_path, 'w', encoding='utf-8', newline='') as file:
                # Obtenemos los nombres de las columnas con las llaves del primer registro
                headers = list_of_students[0].keys()
                # Inicializamos el escritor indicando el archivo destino y los encabezados
                writer = csv.DictWriter(file, fieldnames=headers)
                # Escribimos la primera fila en el documento con los títulos
                writer.writeheader()
                # Insertamos la lista completa de nuestras series
                writer.writerows(list_of_students)
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
                list_of_students.append(Student(student))
            return list_of_students
    except FileNotFoundError:
        print("Archivo no encontrado, Exporte primero el archivo")
            
