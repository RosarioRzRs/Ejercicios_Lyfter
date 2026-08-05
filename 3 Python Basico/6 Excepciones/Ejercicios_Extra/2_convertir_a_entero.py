
def convert_to_int(list):
    message = "Resultado:"
    print(message)
    for record in list:
        try:
            string_to_int = int(record)
            message = f"{record} convertido a {string_to_int}"
            print(message)
        except ValueError:
            print(f"No se pudo convertir el elemento: {record}")


def main():
    my_list = ['4', 'hola', '10', '5.2']
    convert_to_int(my_list)


main()