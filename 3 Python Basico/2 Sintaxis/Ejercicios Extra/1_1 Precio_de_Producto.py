# Cree un programa que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
# Si el precio es menor a 100, el descuento es del 2%.
# Si el precio es mayor o igual a 100, el descuento es del 10%.
# Ejemplos:
# 120 → 108
# 40 → 39.2

#Solicitar precio del producto
product_price = int(input("Ingrese el precio del producto: "))

#Compara si el precio es menor a 100
if product_price < 100:
    discount = product_price * 0.02
else:
    discount = product_price * 0.1

final_price = product_price - discount

#Mostrar precio con el descuento
message = f"El precio final es: {final_price}"
print(message)