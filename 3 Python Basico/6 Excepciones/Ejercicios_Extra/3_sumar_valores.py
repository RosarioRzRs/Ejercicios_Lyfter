
def addition_values(list):
    total_result = 0
    for record in list:
        try:
            string_to_float = float(record)
            total_result = total_result + string_to_float
            message = f"{string_to_float} sumado correctamente"
            print(message)
        except ValueError:
            print(f"Elemento invalido: {record}")
    message = f"Total de la suma: {total_result}"
    print(message)
def main():
    my_list = ['10', 'manzana', '5.5', '3', 'n/a']
    addition_values(my_list)


main()