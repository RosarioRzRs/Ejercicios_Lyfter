def check_name(name):
    incorrect_name = name.isdigit()
    if incorrect_name:
        raise ValueError ("El nombre no puede ser un numero")

    return True


def main():

    while True:
        user_name = input("Ingrese su nombre: ")
        try:
            check_name (user_name)
            break
        except ValueError as ex:
            print(ex)

    while True:
        try:
            user_age = int(input("Ingrese su edad: "))
            if user_age < 1 or user_age > 100:
                raise ValueError()
            break
        except ValueError:
                print("Numero no valido")

    message = f"Hola {user_name}, su edad es {user_age}"
    print(message)
    

            



main()