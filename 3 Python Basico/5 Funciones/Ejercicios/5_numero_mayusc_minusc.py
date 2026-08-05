# Cree una función que imprima el número de mayúsculas y el 
# número de minúsculas en un string.
# “I love Nación Sushi” → 
# “There’s 3 upper cases and 13 lower cases”

def print_number_of_uppercase_and_lowercase_string(my_string):
    counter_uppercase = 0
    counter_lowercase = 0
    for index in range(len(my_string)):
        if my_string[index].isupper():
            counter_uppercase += 1 
        elif my_string[index].islower():
            counter_lowercase += 1
    message = f"There's {counter_uppercase} upper cases and {counter_lowercase} lower cases"
    print(message)


my_string = "I love Nación Sushi"
print_number_of_uppercase_and_lowercase_string(my_string)

