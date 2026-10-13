def validated_bubble_sort(list_of_numbers):
    for element in list_of_numbers:
        if not isinstance(element, (int, float)):
            return 1
    if len(list_of_numbers) == 0:
        return 2
    return 0


def bubble_sort(list_of_numbers):
    lenght_of_list = len(list_of_numbers)-1
    iterations = 0
    swap = 0
    exchange = 0
    for index_main in range (lenght_of_list):
        exchange = 0
        for index in range (lenght_of_list-index_main):
            if list_of_numbers[index + 1] < list_of_numbers[index]:
                print(f"Se intercambia {list_of_numbers[index + 1]} por {list_of_numbers[index]}")
                list_of_numbers[index], list_of_numbers[index + 1] = list_of_numbers[index +1 ], list_of_numbers[index] 
                print(list_of_numbers)
                swap += 1
                exchange += 1
            else:
                print(f"Sin cambios,{list_of_numbers[index]} y {list_of_numbers[index+1]}  se quedan igual")

            iterations += 1
        if exchange == 0:
            break
    print("\n==Lista ordenada ", list_of_numbers)
    print("==Iteraciones = ", iterations)
    print("==Itercambios = ", swap)
        

def main():
    list_of_numbers = [1,2,3,5,4]
    # list_of_numbers = []
    validated_number = validated_bubble_sort(list_of_numbers)
    match validated_number:
        case 0:
            bubble_sort(list_of_numbers)
        case 1:
            print("===Error: La lista contiene al menos un elemeto no numericos===")
        case 2:
            print("===Lista Vacio===")
    


if __name__ =='__main__': 
    main()