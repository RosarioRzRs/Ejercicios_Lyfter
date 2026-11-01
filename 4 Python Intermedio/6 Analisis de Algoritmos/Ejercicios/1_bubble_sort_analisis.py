def bubble_sort(list_of_numbers):
    lenght_of_list = len(list_of_numbers)-1     # O(1)
    iterations = 0      #O(1)
    for index_main in range (lenght_of_list):   # O(n)
        for index in range (lenght_of_list-index_main):      # O(log n)
            if list_of_numbers[index + 1] < list_of_numbers[index]:       # O(1)
                print(f"Se intercambia {list_of_numbers[index + 1]} por {list_of_numbers[index]}")     # O(1)
                list_of_numbers[index], list_of_numbers[index + 1] = list_of_numbers[index +1 ], list_of_numbers[index]      # O(1)
                iterations += 1      # O(1)
            else:
                print(f"Sin cambios,{list_of_numbers[index]} y {list_of_numbers[index+1]}  se quedan igual")     # O(1)
        if iterations == 0:  # O(1)
            break           # O(1)
    print("Iteraciones totales = ", iterations)     # O(1)
        

def main():
    list_of_numbers = [105,5,9,40,80,4,2000,7,8,90,2,100,1,1000]      # O(1)
    # list_of_numbers = [1,2,3,4,5,6,7,8,9]
    new_list = bubble_sort(list_of_numbers)        # O(log n)
    print(list_of_numbers)       # O(1)
    


if __name__ =='__main__':  # O(1)
    main()           # O(log n)