# Cree una clase de User que:
# Tenga un atributo de date_of_birth.
# Tenga un property de age.
# Luego cree un decorador para funciones que acepten un User 
# como parámetro que se encargue de revisar si el User es mayor 
# de edad y arroje una excepción de no ser así.
#Se importa datetime para obtener la fecha
from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
       
    @property
    def age(self):
        today = date.today()
        less_1 = (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        return today.year - self.date_of_birth.year - less_1


def user_is_of_legal_age(func):
    def wrapper (user):
        try:
            if user.age < 18:
                raise ValueError (f"El usuario es menor de Edad. Tiene {user.age} años ")
            func(user)
        except ValueError as ex:
            print(ex)
    return wrapper


@user_is_of_legal_age
def print_if_user_is_of_legal_age(user):
    print(f"El usuario es mayor de edad. Tiene {user.age} años ")

new_user = User(date(1990,11,2))
print_if_user_is_of_legal_age(new_user)


