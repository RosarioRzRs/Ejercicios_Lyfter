def bubble_sort(list_of_numbers):
    lenght_of_list = len(list_of_numbers)-1     # O(1)
    for index_main in range (lenght_of_list):   # O(n)
        iterations = 0      #O(1)
        for index in range (lenght_of_list-index_main):      # O(n)
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
    new_list = bubble_sort(list_of_numbers)        # O(n^2)
    print(list_of_numbers)       # O(1)
    


if __name__ =='__main__':  
    main()           # O(n^2)


 
# ¿la cantidad de elementos se va dividiendo a la mitad o va bajando de uno en uno?
# ##### DISMINUYE 1 EN 1 
# Preguntas:
# ¿Cuál es la complejidad de cada versión?
####   # O(n^2)
# mejor caso y peor caso:
# Mejor caso es la implementacion de braek e index_main ya que se evitar comparar
# los ultimos elementos de la lista conforme pasa las iteracciones ya que estos ya son
# los mayores. En el caso del break si en un ciclo no se detecto que hubo un intercambio
# significa que estan en orden. cuando se llega a la linea 12, como no hubo cambios 
# se rompe el ciclo ya que no es necesario
