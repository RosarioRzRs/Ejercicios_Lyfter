def validated_bubble_sort(list_of_numbers):
    if len(list_of_numbers) == 0:
        raise ValueError("Lista Vacia")
    for element in list_of_numbers:
        if isinstance(element, bool) or not isinstance(element, (int, float)):
            raise ValueError("Error: La lista contiene elementos no númericos")
    iterations, swap= bubble_sort(list_of_numbers)
    print("\n==Lista ordenada ", list_of_numbers)
    print("==Iteraciones = ", iterations)
    print("==Intercambios = ", swap)
    return True


def bubble_sort(list_of_numbers):
    length_of_list = len(list_of_numbers)-1
    iterations = 0
    swap = 0
    for index_main in range (length_of_list):
        exchange = False
        for index in range (length_of_list-index_main):
            if list_of_numbers[index + 1] < list_of_numbers[index]:
                print(f"Se intercambia {list_of_numbers[index + 1]} por {list_of_numbers[index]}")
                list_of_numbers[index], list_of_numbers[index + 1] = list_of_numbers[index +1 ], list_of_numbers[index] 
                print(list_of_numbers)
                swap += 1
                exchange = True
            else:
                print(f"Sin cambios,{list_of_numbers[index]} y {list_of_numbers[index+1]}  se quedan igual")

            iterations += 1
        if not exchange:
            break
    return iterations, swap
   
        

def main():
    # list_of_numbers = [1,2,3,5,4]
    # list_of_numbers = []
    # list_of_numbers = [1,"HOLA",5]
    list_of_numbers = [True, 5]
    try:
        validated_bubble_sort(list_of_numbers)
      
    except ValueError as ex:
        print(ex)
   
    


if __name__ =='__main__': 
    main()