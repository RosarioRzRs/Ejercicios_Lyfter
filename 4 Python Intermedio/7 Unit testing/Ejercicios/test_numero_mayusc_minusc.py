from numero_mayusc_minusc import count_number_of_uppercase_and_lowercase_string
import pytest

def test_count_number_of_uppercase_and_lowercase_string_check_counter_correctly():
    # AAA
    #Arrange
    my_string = "I love Nación Sushi"
   #Act
    counter_lowercase, counter_uppercase= count_number_of_uppercase_and_lowercase_string(my_string)
    #Assert
    assert 13 == counter_lowercase and 3 == counter_uppercase


def test_count_number_of_uppercase_and_lowercase_string_check_counter_correctly_omit_number():
    # AAA
    #Arrange
    my_string = "I love Nación 583 Sushi 1000-"
   #Act
    counter_lowercase, counter_uppercase= count_number_of_uppercase_and_lowercase_string(my_string)
    #Assert
    assert 13 == counter_lowercase and 3 == counter_uppercase


def test_count_number_of_uppercase_and_lowercase_string_check_parameter_isnot_a_string():
    # AAA
    #Arrange
    my_string = 2565
    #Act & Assert
    with pytest.raises(ValueError):
        count_number_of_uppercase_and_lowercase_string(my_string)