def repeat_twice(func):
    def wrapper(name):
        for index in range (0,2):
            func(name)
    return wrapper

@repeat_twice
def print_name(name):
    print(f"Hola, {name}")


print_name("Rosario")
   

