# Dada una lista de ventas con la siguiente información:
# date
# customer_email
# items
# Y cada item teniendo la siguiente información:
# name
# upc
# unit_price
# Cree un diccionario que guarde el total de ventas de cada UPC.

#Se define lista y diccionario
sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]
result_upc = {}
#Se crea diccionario y se hace sumatoria
for index in range (len(sales)):
    for index_items in range (len(sales[index]['items'])):
        items_of_list = sales[index]['items'][index_items]['upc']
        items_of_directinary = result_upc.get(items_of_list)
        if items_of_directinary == None:
            result_upc[items_of_list] = sales[index]['items'][index_items]['unit_price']
        else:
            result_upc[items_of_list] = result_upc[items_of_list] + sales[index]['items'][index_items]['unit_price']
#Se imprime diccinario      
message = result_upc 
print(message)

