from suma_lista import add_number_of_list

def test_suma_lista_check_with_positive_number():
    #AAA
    #Arrange
    my_list = [4, 6, 2, 29]
    #Act
    sum = add_number_of_list(my_list)
    #Assert
    assert sum == 41


def test_suma_lista_check_with_negative_number():
    #AAA
    #Arrange
    my_list = [4, -6, 2, -29]
    #Act
    sum = add_number_of_list(my_list)
    #Assert
    assert sum == -29


def test_suma_lista_check_with_empty_list():
    #AAA
    #Arrange
    my_list = []
    #Act
    sum = add_number_of_list(my_list)
    #Assert
    assert sum == 0

