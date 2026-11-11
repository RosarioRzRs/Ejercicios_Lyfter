import menu, action, data

def main():

    list_of_students = []
    while True:
        print("""
        =================================================
            SISTEMA DE CONTROL DE ESTUDIANTES
        =================================================
        """)
        option_number = menu.selection()
        match option_number:
            case 1: 
                action.add_information(list_of_students)
            case 2: 
                action.show_information(list_of_students)
            case 3: 
                action.show_top_3_the_better_of_students(list_of_students)
            case 4: 
                action.show_failing_students(list_of_students)
            case 5: 
                action.show_average_of_students(list_of_students)
            case 6: 
                action.delete_student(list_of_students) 
            case 7: 
                data.save_list_of_students('1 OOP/Ejercicios/Sistema de Control de Estudiantes.csv',list_of_students)  
            case 8: 
                list_of_students = data.read_list_of_students('1 OOP/Ejercicios/Sistema de Control de Estudiantes.csv')
            case 9: 
                break
        input("\nPresione ENTER para continuar ")             
        


if __name__ =='__main__': 
    main()