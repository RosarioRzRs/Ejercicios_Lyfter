class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        message = "Hace un sonido"
        return message

class Dog(Animal):
    def speak(self):
        message = "Guau"
        return message

class Cat(Animal):
    def speak(self):
        message = "Miau"
        return message



dog = Dog("Firulais")
cat = Cat("Kitty")

print(dog.name)
print(dog.speak())
print(cat.name)
print(cat.speak())