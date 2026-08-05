def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def count_words(content):
    words = content.split()
    return len(words)


def main():
    text = read_file("Ejercicios/Manejo de Archivos/Ejercicios_Extra/ejercicio_extra_2.txt")
    print(text)
    total_of_word = count_words(text)
    message = f"Este archivo contiene {total_of_word} palabras"
    print(message)

    
main()