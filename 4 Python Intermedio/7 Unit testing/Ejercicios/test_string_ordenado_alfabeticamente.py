from string_ordenado_alfabeticamente import sort_alphabetically
import pytest

def test_string_ordenado_alfabeticamente_order_correctly():
    #AAA
    #Arrange
    my_string = "python-variable-funcion-computadora-monitor"
    #Act
    message = sort_alphabetically(my_string)
    #Assert
    assert message == "computadora-funcion-monitor-python-variable"


def test_string_ordenado_alfabeticamente_parameter_isnot_a_string():
     # AAA
    #Arrange
    my_string = 2565
    #Act & Assert
    with pytest.raises(ValueError):
        sort_alphabetically(my_string)


def test_string_ordenado_alfabeticamente_order_words_with_number_correctly():
    #AAA
    #Arrange
    my_string = "python-8974-variable-funcion-1258-computadora-monitor"
    #Act
    message = sort_alphabetically(my_string)
    #Assert
    assert message == "1258-8974-computadora-funcion-monitor-python-variable"