def bubble_sort(list_of_numbers):
    lenght_of_list = len(list_of_numbers)-1
    iterations = 0
    for index_main in range (lenght_of_list):
        for index in range (lenght_of_list, 0 + index_main, -1):
            if list_of_numbers[index - 1] > list_of_numbers[index]:
                print(f"Se intercambia {list_of_numbers[index - 1]} por {list_of_numbers[index]}")
                list_of_numbers[index], list_of_numbers[index - 1] = list_of_numbers[index -1 ], list_of_numbers[index] 
                iterations += 1
            else:
                print(f"Sin cambios,{list_of_numbers[index]} y {list_of_numbers[index-1]}  se quedan igual")
        if iterations == 0:
            break
    print("Iteraciones totales = ", iterations)
        

def main():
    list_of_numbers = [105,5,9,40,80,4,2000,7,8,90,2,100,1,1000]
    # list_of_numbers = [10,1,2,3,4,5,6,7,8,9]
    bubble_sort(list_of_numbers)
    print(list_of_numbers)
    


if __name__ =='__main__': 
    main()