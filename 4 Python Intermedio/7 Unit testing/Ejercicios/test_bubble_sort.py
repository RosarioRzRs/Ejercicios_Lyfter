from bubble_sort import bubble_sort
import random
import pytest

def test_bubble_sort_check_with_a_little_list():
    # AAA
    #Arrange
    list_of_numbers = [105,5,9,40,80,4,2000,7,8,90]
    #Act
    # new_list_of_numbers = bubble_sort(list_of_numbers)
    bubble_sort(list_of_numbers)
    #Assert
    assert list_of_numbers == [4,5,7,8,9,40,80,90,105,2000]


def test_bubble_sort_check_with_more_100_items():
    # AAA
    #Arrange
    list_of_numbers = [random.randint(1,1000) for _ in range(10)]
    unordered_list = list_of_numbers.copy()
    #Act
    bubble_sort(list_of_numbers)
    #Assert
    assert list_of_numbers == sorted(unordered_list)


def test_bubble_sort_check_with_empty_list():
    # AAA
    #Arrange
    list_of_numbers = []
    #Act
    bubble_sort(list_of_numbers)
    #Assert
    assert list_of_numbers == []


def test_bubble_sort_check_parameter_is_not_a_list_send_a_raise():
    # AAA
    #Arrange
    list_of_numbers = "gato"
    #Act & Assert
    with pytest.raises(ValueError):
        bubble_sort(list_of_numbers)
    