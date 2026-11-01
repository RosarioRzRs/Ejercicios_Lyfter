def bubble_sort_steps(list_of_numbers):
    length_of_list = len(list_of_numbers)-1
    iterations = 0
    swap = 0
    exchange = False
    for index_main in range (length_of_list):
        exchange = 0
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
    list_of_numbers = [5,4,3,1,2]
    # list_of_numbers = [1,2,3,4,5,6,7,8,9]
    iterations, swap = bubble_sort_steps(list_of_numbers)
    print("\nLista ordenada ", list_of_numbers)
    print("Iteraciones = ", iterations)
    print("Intercambios = ", swap)

if __name__ =='__main__': 
    main()