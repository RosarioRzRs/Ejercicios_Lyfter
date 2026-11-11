# Cree una función que imprima el número de mayúsculas y el 
# número de minúsculas en un string.
# “I love Nación Sushi” → 
# “There’s 3 upper cases and 13 lower cases”

def count_number_of_uppercase_and_lowercase_string(my_string):
    if not isinstance(my_string, str):
        raise ValueError("El parametro debe ser un string")
    counter_uppercase = 0
    counter_lowercase = 0
    for index in range(len(my_string)):
        if my_string[index].isupper():
            counter_uppercase += 1 
        elif my_string[index].islower():
            counter_lowercase += 1
    
    return counter_lowercase, counter_uppercase

if __name__ == "__main__":
    # my_string = "I love Nación Sushi"
    # my_string = 2565
    my_string = ""
    try:
        counter_lowercase, counter_uppercase = count_number_of_uppercase_and_lowercase_string(my_string)
        message = f"There're {counter_uppercase} upper cases and {counter_lowercase} lower cases"
        print(message)
    except ValueError as ex:
        print(ex)

