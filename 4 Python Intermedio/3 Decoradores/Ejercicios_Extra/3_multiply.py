from datetime import datetime
from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        print(f"func: {func.__name__} - args: {args} - [{datetime.today()}] - Resultado: {result}")
        return result
    return wrapper


def validate_numbers(func):
    @wraps(func)
    def wrapper(*args):
        for record in args:
            if not isinstance(record, (int, float)):
                raise ValueError("Hay un elemento que no es un numero")
        return func(*args) 
    return wrapper

@log_call
@validate_numbers
def multiply(*args):
    result = 1
    for record in args:
        result *= record
    
    return result


try:
    result = multiply(3,4)
    # result = multiply("hola",4)
    print(f"Resultado {result}")
except ValueError as ex:
    print(ex)