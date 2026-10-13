# Cree una clase de Bus con:
# Un atributo de max_passengers.
# Un método para agregar pasajeros uno por uno 
#(que acepte como parámetro una instancia de la clase Person vista
#en la lección). Este solo debe agregar pasajeros si lleva menos 
#de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
# Un método para bajar pasajeros uno por uno (en cualquier orden).

class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
    

class Bus:
    
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.list_passengers = []

    def add_passenger(self, passenger):
        self.list_passengers.append(passenger)

    def delete_passenger(self):
        deleted_passenger = self.list_passengers.pop(0)


def is_valid_name(name):
    if not name.strip():
        print("Nombre vacio, ingrese nuevamente")
        return False
    elif any(char.isdigit() for char in name):
        print("Nombre ingresado tiene al menos un numero, ingrese nuevamente")
        return False
    return True


def choose_option():
    while True:
        message = """
            1 Agregar pasajero
            2 Bajar pasajero
            3 Cerrar 
            """
        print(message)
        next_step = 0
        try:
            option_number = int (input("Ingrese una opcion: "))
            next_step = 1
        except ValueError:
            print("El valor ingresado no es un numero, ingrese nuevamente")

        while next_step == 1:
            try:
                if option_number > 3 or option_number < 1:
                    raise ValueError()
                else:
                    next_step = 2
                    break
            except ValueError:
                print("El valor ingresado no es una opcion valida, ingrese nuevamente")
                break
        if next_step == 2:
            break
    return option_number


def capture_passenger_data():
    while True:
        passenger_name = input("Ingrese nombre del pasajero: ")
        if is_valid_name(passenger_name):
            break

    while True:
        try:
            passenger_age = int(input("Ingrese la edad del pasajero: "))
            if passenger_age < 1 or passenger_age > 100:
                raise ValueError()
            break
        except ValueError:
            print("Numero no valido")

    return passenger_name, passenger_age


def main():
    cdmx_bus = Bus(3)
    while True:
        option_number = choose_option()

        match option_number:
            case 1:
                if len(cdmx_bus.list_passengers) < cdmx_bus.max_passengers:
                    name, age = capture_passenger_data ()
                    passenger_data = Person(name, age)
                    cdmx_bus.add_passenger(passenger_data)
                    print("======== Se agrego el pasajero exitosamente ========")
                else:
                    print("*********** El bus esta lleno ***********")
                
            case 2:
                if not len(cdmx_bus.list_passengers) == 0:
                    cdmx_bus.delete_passenger()
                    print("======== Se bajo un pasajero exitosamente ========")
                else:
                    print("*********** El bus esta vacio ***********")

            case 3:
                break


if __name__ == "__main__":
    main()