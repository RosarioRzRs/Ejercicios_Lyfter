# Dada una lista de productos vendidos, 
# donde cada uno tiene categoría y precio, 
# cree un diccionario que acumule el total por categoría.

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
result_category = {}
#Se crea diccionario y se hace sumatoria por categoria
for index in range (len(products)):
        category_of_list = products[index]['category']
        category_of_directinary = result_category.get(category_of_list)
        if category_of_directinary == None:
            result_category[category_of_list] = products[index]['price']
        else:
            result_category[category_of_list] = result_category[category_of_list] + products[index]['price']
#Se imprime diccinario      
message = result_category 
print(message)
