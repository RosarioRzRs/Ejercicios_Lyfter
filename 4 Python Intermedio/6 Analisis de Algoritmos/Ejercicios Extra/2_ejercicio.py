# Considere los siguientes dos algoritmos:

def linear_search(my_list, target):
    for item in my_list:   # O(n)
        if item == target:  # O(1)
            return True   # O(1)
    return False    # O(1)


def binary_search(my_list, target):
    low = 0     # O(1)
    high = len(my_list) - 1    # O(1)
    while low <= high:    # O(log n)
        mid = (low + high) // 2     # O(1)
        if my_list[mid] == target:    # O(1) 
            return True    # O(1)
        elif my_list[mid] < target:   # O(1)
            low = mid + 1   # O(1)
        else:
            high = mid - 1    # O(1)
    return False    # O(1)


# Preguntas:
# ¿Cuál es la complejidad de cada algoritmo?
#   la primera funcion es O(n), y la segunda es O(log n)
# ¿En qué condiciones conviene usar cada uno?
#   la primera  cuando se tenga un tamano de lista pequeña
# se la lista es muy grande conviene la segunda funcion para
#  evitar tiempos de ejecucion alto
# ¿Qué pasa si la lista no está ordenada?   
#   Si no esta ordenada conviene usar la primera funcion. 
#  En el caso de la segunda, no seria muy factible, a menos que se 
# ordene previamente