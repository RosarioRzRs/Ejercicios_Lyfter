from numero_primo import evaluate_prime_number
import pytest

def test_evaluate_prime_number_check_selected_correctly():
    #AAA
    #Arrange
    my_list_prime_number = [1, 4, 6, 7, 13, 9, 67]
    #Act
    new_list = evaluate_prime_number(my_list_prime_number)
    #Assert
    assert new_list == [7,13,67]

def test_evaluate_prime_number_check_elements_isnot_a_list():
    #AAA
    #Arrange
    my_list_prime_number = 8
    #Act & Assert
    with pytest.raises(ValueError):
        evaluate_prime_number(my_list_prime_number)


def test_evaluate_prime_number_check_parameter_isnot_a_integer_number():
    #AAA
    #Arrange
    my_list_prime_number = [1, 4, 6, 7, 13.2, 9, 67.8]
    #Act & Assert
    with pytest.raises(ValueError):
        evaluate_prime_number(my_list_prime_number)