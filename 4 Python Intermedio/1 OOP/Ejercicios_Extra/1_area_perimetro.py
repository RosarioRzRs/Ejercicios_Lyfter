class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter

def request_measures():
    width = int(input("Ingrese la  altura: "))
    height = int(input("Ingrese el ancho: "))

    return width, height

def main():
    width, height = request_measures()
    rectangle = Rectangle(width, height)
    try:   
        if width < 0 or height < 0:
            raise ValueError()

        print(rectangle.get_area())
        print(rectangle.get_perimeter())
    except ValueError as ex:
        print("Existe un valor negativo, los valores deben ser positivos")
        # raise ex
    
  

main()

        

