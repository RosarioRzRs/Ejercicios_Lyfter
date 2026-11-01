# Cree una clase de Circle con:
# Un atributo de radius (radio).
# Un método de get_area que retorne su área.

class Circle:
    radius = 5

    def get_area(self):
        area = 3.1416 * pow(self.radius, 2)
        return area


my_circle = Circle()
circle_area = my_circle.get_area()
message = f"El area del circulo con radio {my_circle.radius} es {circle_area}"
print(message)