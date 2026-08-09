
def is_valid_name(name):
    if not name.strip():
        print("Nombre vacio, ingrese nuevamente")
        return False
    elif any(char.isdigit() for char in name):
        print("Nombre ingresado tiene al menos un numero, ingrese nuevamente")
        return False
    return True


def is_valid_section(section):
    if len(section)==3 and section[0].isdigit() and section[1].isdigit() and section[2].isalpha():
            return True
    else:
        print("Seccion no cumple con el formato (10A), ingrese nuevamente")
        return False


def student_exists(list_of_students, name, section):
    for student in list_of_students:
        if student['name'] == name and student['section'] == section:
            return True
    return False
    

def add_information(list_of_students):
    print("====================== Ingresar nuevos Estudiantes al Sistema de Control de Estudiantes ======================\n")
    while True:
        try:
            students_number_to_add = int(input("Cuantos estudiantes desea agregar: "))
            break
        except ValueError:
            print("El valor ingresado no es un numero, ingrese nuevamente")

    for index in range (students_number_to_add):

        while True:
            while True:
                student_name = input("Nombre Completo: ").upper()
                if is_valid_name(student_name):
                    break

            while True:
                section = input("Seccion: ").upper()
                if is_valid_section(section):
                    break

            if not student_exists(list_of_students, student_name, section):
                break 
            else:
                print("El estudiante ya existe, ingrese otro estudiante")

        while True:
            try:
                spanish_note = int(input("Nota de Español: "))
                if spanish_note > 100 or spanish_note < 0:
                    raise ValueError ("rango incorrecto")
                break
            except ValueError as error:
                if str(error) == "rango incorrecto":
                    print("La nota debe estar entre 0-100, ingrese nuevamente")
                else:
                    print("La nota no es un numero, ingrese nuevamente")
        while True:
            try:
                english_note = int(input("Nota de Ingles: "))
                if english_note > 100 or english_note < 0:
                    raise ValueError ("rango incorrecto")
                break
            except ValueError as error:
                if str(error) == "rango incorrecto":
                    print("La nota debe estar entre 0-100, ingrese nuevamente")
                else:
                    print("La nota no es un numero, ingrese nuevamente")
        while True:
            try:
                social_note = int(input("Nota de Sociales: "))
                if social_note > 100 or social_note < 0:
                    raise ValueError ("rango incorrecto")
                break
            except ValueError as error:
                if str(error) == "rango incorrecto":
                    print("La nota debe estar entre 0-100, ingrese nuevamente")
                else:
                    print("La nota no es un numero, ingrese nuevamente")
        while True:
            try:
                science_note = int(input("Nota de Ciencias: "))
                if science_note > 100 or science_note < 0:
                    raise ValueError ("rango incorrecto")
                break
            except ValueError as error:
                if str(error) == "rango incorrecto":
                    print("La nota debe estar entre 0-100, ingrese nuevamente")
                else:
                    print("La nota no es un numero, ingrese nuevamente")
        average_note = (spanish_note + english_note + social_note + science_note)/4
        dict_student = {
            'name': student_name,
            'section': section,
            'spanish_note': spanish_note, 
            'english_note': english_note, 
            'social_note': social_note, 
            'science_note': science_note,
            'average_note' : average_note,
            }
        
        list_of_students.append(dict_student)


def show_information(list_of_students):
    if len(list_of_students) > 0:
        print("====================== Mostrar informacion del Sistema de Control de Estudiantes ======================\n")
        for student in list_of_students:
            show_student = f"-Nombre  completo: {student['name']}\n"
            show_student += f"-Sección: {student['section']}\n"
            show_student += "Notas:\n"
            show_student += f"-Español:  {student['spanish_note']}\n"
            show_student += f"-Inglés:   {student['english_note']}\n"
            show_student += f"-Sociales: {student['social_note']}\n"
            show_student += f"-Ciencias: {student['science_note']}\n"
            print(show_student)
    else:
        show_student = "************* Listado de Estudiantes Vacio *************\n"
        print(show_student)
    

def show_top_3_the_better_of_students(list_of_students):
    if len(list_of_students) > 0:
        print("====================== Mostrar informacion Top 3 de los mejores Estudiantes ======================\n")
        list_top_3_students = sorted(list_of_students, key=lambda x: x['average_note'], reverse = True)
    
        for index, student in enumerate(list_top_3_students):
            show_student = f"-Nombre  completo: {student['name']}\n"
            show_student += f"-Sección: {student['section']}\n"
            show_student += "Notas:\n"
            show_student += f"-Español:  {student['spanish_note']}\n"
            show_student += f"-Inglés:   {student['english_note']}\n"
            show_student += f"-Sociales: {student['social_note']}\n"
            show_student += f"-Ciencias: {student['science_note']}\n"
            show_student += f"*Promedio de las Notas: {student['average_note']}\n"
            print(show_student)
            if index == 2:
                break
    else:
        show_student = "************* Listado de Estudiantes Vacio *************\n"
        print(show_student)


def show_failing_students(list_of_students):
    if len(list_of_students) > 0:
        print("====================== Mostrar informacion de Estudiantes Reprobados ======================\n")
        for student in list_of_students:
            if student['spanish_note'] < 60 or student['english_note'] < 60 or student['social_note'] < 60 or student['science_note'] < 60:
                show_student = f"-Nombre  completo: {student['name']}\n"
                show_student += f"-Sección: {student['section']}\n"
                show_student += "Notas:\n"
                if student['spanish_note'] < 60:
                    show_student += f"-Español:  {student['spanish_note']}\n"
                if student['english_note'] < 60:
                    show_student += f"-Inglés:   {student['english_note']}\n"
                if student['social_note'] < 60:
                    show_student += f"-Sociales: {student['social_note']}\n"
                if student['science_note'] < 60:
                    show_student += f"-Ciencias: {student['science_note']}\n"
                print(show_student)
    else:
        show_student = "************* Listado de Estudiantes Vacio *************\n"
        print(show_student)


def show_average_of_students(list_of_students):
    if len(list_of_students) > 0:
        print("====================== Mostrar informacion de Estudiantes (Promedio de Notas) ======================\n")
        for student in list_of_students:
            show_student = f"-Nombre  completo: {student['name']}\n"
            show_student += f"-Sección: {student['section']}\n"
            show_student += "Notas:\n"
            show_student += f"-Español:  {student['spanish_note']}\n"
            show_student += f"-Inglés:   {student['english_note']}\n"
            show_student += f"-Sociales: {student['social_note']}\n"
            show_student += f"-Ciencias: {student['science_note']}\n"
            show_student += f"*Promedio de las Notas: {student['average_note']}\n"
            print(show_student)
    else:
        show_student = "************* Listado de Estudiantes Vacio *************\n"
        print(show_student)


def delete_student(list_of_students):
    if len(list_of_students) > 0:
        print("====================== Eliminar Estudiante del Sistema ======================\n")
        while True:
            while True:
                student_name = input("Nombre Completo: ").upper()
                if is_valid_name(student_name):
                    break

            while True:
                section = input("Seccion: ").upper()
                if is_valid_section(section):
                    break

            if student_exists(list_of_students, student_name, section):
                confirm_deleted = input("Escriba (Si) para eliminar el estudiante del listado: ").upper()
                if confirm_deleted == "SI":
                    for index, student in enumerate(list_of_students):
                        if student['name'] == student_name and student['section'] == section:
                            deleted_student = list_of_students.pop(index)
                            print("El estudiante ha sido Eliminado con Exito")
                            break
                    break
                else:
                    print("Respuesta incorrecta, Accion Cancelada")
                    break
            else:
                print("El estudiante no existe")
                break
        
    else:
        show_student = "************* Listado de Estudiantes Vacio *************\n"
        print(show_student)


