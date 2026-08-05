def read_file(path):
    line_to_line = []
    with open(path, 'r', encoding='utf-8') as file:
        for lines in file:
            line_to_line.append(lines.strip())
    return line_to_line   


def write_new_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)


def main():
    list_of_lines = read_file('Ejercicios/Manejo de Archivos/Ejercicios_Extra/ejercicio_extra_1.txt')
    print (list_of_lines)
    text = " ".join(list_of_lines)
    print(text)
    write_new_file('Ejercicios/Manejo de Archivos/Ejercicios_Extra/ejercicio_extra_1_2.txt', text)
    

main()