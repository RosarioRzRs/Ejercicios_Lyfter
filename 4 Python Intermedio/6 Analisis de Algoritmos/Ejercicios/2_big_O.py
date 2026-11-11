#     print_numbers_times_2

def print_numbers_times_2(numbers_list):  # O(n)
	for number in numbers_list:      # O(n) 
		print(number * 2)          # O(1)


#     check_if_lists_have_an_equal

def check_if_lists_have_an_equal(list_a, list_b):   # O(a x b)
	for element_a in list_a:         # O(a) 
		for element_b in list_b:     # O(b)
			if element_a == element_b:   # O(1)
				return True       # O(1)
				
	return False     # O(1)

#Peor y mejor caso:
# Peor: si no tuviera el return True, seguiria evaluando  aunque haya encontrado
# al inicio o al final o no lo haya encontrado.
# Mejor: si esta al inicio de las listas, no tiene que seguir comparando con el resto 
# de los elementos de las listas

#    print_10_or_less_elements

def print_10_or_less_elements(list_to_print):    # O(1)
	list_len = len(list_to_print)      # O(1)
	for index in range(min(list_len, 10)):   # O(1)
		print(list_to_print[index])    # O(1)


#   generate_list_trios

def generate_list_trios(list_a, list_b, list_c):    # O(a x b x c)
	result_list = []     # O(1)
	for element_a in list_a:     # O(a)
		for element_b in list_b:   # O(b)
			for element_c in list_c:   # O(c)
				result_list.append(f'{element_a} {element_b} {element_c}')  # O(1)
				
	return result_list  # O(1)