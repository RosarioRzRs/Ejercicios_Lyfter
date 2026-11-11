from cadena import string
import pytest

def test_string_check_with_letters():
    #AAA
    #Arrange
    my_string = "Hola mundo"
    #Act
    message = string(my_string)
    #Assert
    assert message == "odnum aloH"


def test_string_check_with_empty_string():
    #AAA
    #Arrange
    my_string = ""
    #Act
    message = string(my_string)
    #Assert
    assert message == ""


def test_string_check_parameter_isnot_a_string():
    # AAA
    #Arrange
    my_string = 2565
    #Act & Assert
    with pytest.raises(ValueError):
        string(my_string)