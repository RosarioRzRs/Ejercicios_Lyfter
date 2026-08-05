def read_file(path):
    line_to_line = []
    with open(path, 'r', encoding='utf-8') as file:
        for lines in file:
            line_to_line.append(lines.strip())
    return line_to_line   

def write_file(path, text_list):
    with open(path, 'w', encoding='utf-8') as file:
        for upper_text in text_list:
            file.write(upper_text + "\n")

def main():
   
    text_list = read_file("Ejercicios/Manejo de Archivos/Ejercicios_Extra/ejercicio_extra_3.txt")
    for index, record in enumerate(text_list):
        text_list[index] = record.upper()
    write_file("Ejercicios/Manejo de Archivos/Ejercicios_Extra/ejercicio_extra_3_2.txt", text_list)

main()