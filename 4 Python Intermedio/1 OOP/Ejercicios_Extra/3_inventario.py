class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

class Inventory:
    def __init__(self):
        self.product_list = []


    def add_product(self, product):
        self.product_list.append(product)


    def show_products(self):
        if len(self.product_list) == 0:
            print ("**** Lista de productos vacia ****")
        else:
            for product in self.product_list:
                message = f"Nombre = {product.name}\n"
                message += f"Precio = {product.price}\n"
                message += f"Cantidad = {product.amount}\n"
                print(message)


    def calculate_total_value_of_inventory(self):
        total_value_of_inventory = 0
        
        if len(self.product_list) > 0:
            for product in self.product_list:
                total_value_of_inventory += product.price * product.amount

        return total_value_of_inventory

def menu():
    message = """Menu:
                    1 Agregar Producto
                    2 Mostar todos los productos
                    3 Calcular el valor total del inventario
                    4 Cerrar menu
                    """
    print(message)
    option_number = int(input("Opcion a elegir: "))
    return option_number


def main():
    product1 = Product("Mouse", 5000,3)
    product2 = Product("Teclado", 8000,2)

    product = Inventory()
    while True:
        option_number = menu()
        match option_number:
            case 1:
                print("====== Agregando producto =====")
                product.add_product(product1)
                product.add_product(product2)
            case 2:
                print("====== Inventario =====")
                product.show_products()
            case 3:
                print("====== Calculo total del inventario =====")
                print(f"Total: {product.calculate_total_value_of_inventory()}")
            case 4:
                break

if __name__ == '__main__':
    main()

        


