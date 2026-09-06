

user_logged_in = True

def requires_login(func):
    def wrapper():
        try:
            if not user_logged_in:
                raise ValueError("Usiario no autenticado")
            func()
        except ValueError as ex:
            print(ex)
    return wrapper


@requires_login
def view_profile():
    print("Mostrando perfil del usuario")

view_profile()