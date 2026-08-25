from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * 3.1416 * self.radius

    def calculate_area(self):
        return 3.1416 * math.sqrt(self.radius)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side * self.side
    
class Rectangule(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_perimeter(self):
        return (self.base * 2) + (self.height * 2)

    def calculate_area(self):
        return self.base * self.height



circle = Circle(5)
square = Square(5)
rectangule = Rectangule(5, 10)

message = f"===Circulo===\n"
message += f"Perimetro: {circle.calculate_perimeter()}\n"
message += f"Area: {circle.calculate_area()}\n"
message += f"===Cuadrado===\n"
message += f"Perimetro: {square.calculate_perimeter()}\n"
message += f"Area: {square.calculate_area()}\n"
message += f"===Rectangulo===\n"
message += f"Perimetro: {rectangule.calculate_perimeter()}\n"
message += f"Area: {rectangule.calculate_area()}\n"
print(message)