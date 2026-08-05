# Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
# Ejemplos:
# first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]
# second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’] ->
# Hay casos
# en los
# que la
# iteracion por
# indice es
# muy util

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]
#imprimir listas por indice
for index in range(0, len(first_list)):
    record_1 = first_list[index]
    record_2 = second_list[index]
    message = f"{record_1} {record_2}"
    print(message)
