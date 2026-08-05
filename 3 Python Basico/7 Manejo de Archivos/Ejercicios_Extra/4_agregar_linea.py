def append_to_file(path, extra_text):
    with open(path, 'a', encoding='utf-8') as file:
        file.write("\n" + extra_text)


def main():
    user_text = input ("Ingrese una linea de texto: ")
    append_to_file('Ejercicios/Manejo de Archivos/Ejercicios_Extra/ejercicio_extra_4.txt', user_text)


main()