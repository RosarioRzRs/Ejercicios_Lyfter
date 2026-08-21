# Cree un programa que lea nombres de canciones de un archivo (línea por línea)
# y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def read_list_of_songs(path):
    list_of_songs = []
    with open(path, 'r', encoding='utf-8') as file:
        for lines in file:
            list_of_songs.append(lines.strip())
    return list_of_songs   


def write_new_list_of_song(path, list):
    with open(path, 'w', encoding='utf-8') as file:
        for song in list:
            file.write(song + "\n")


def main():
    list_of_songs = read_list_of_songs('Ejercicios/Manejo de Archivos/Ejercicios/canciones.txt')
    print (list_of_songs)

    sorted_song_list = sorted(list_of_songs)
    print(sorted_song_list)
    write_new_list_of_song('Ejercicios/Manejo de Archivos/Ejercicios/canciones_ordenado.txt', sorted_song_list)
    

main()