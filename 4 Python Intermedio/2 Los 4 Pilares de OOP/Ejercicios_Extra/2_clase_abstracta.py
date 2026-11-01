from abc import ABC, abstractmethod

#Crear la clase base, crear los 2 metodos abstarctos
class User(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass
#crear las clases hijas
class AdminUser(User):
    def get_role(self):
        print(f"{self.name}, es un administrador")
        
    def has_permission(self, permission):
            if permission == "write" or permission == "read" or permission == "delete" or permission == "create" :
                return True
            return False

class RegularUser(User):
    def get_role(self):
            print(f"{self.name}, es un usuario regular")

    def has_permission(self, permission):
        if permission == "read":
            return True
        return False

#Crear los objetos
user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")
#Imprimir si tienen permiso de acuerdo 
print(user1.has_permission("delete"))  # True
print(user2.has_permission("delete"))  #   False