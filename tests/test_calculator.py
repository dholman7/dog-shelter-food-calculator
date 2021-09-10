import pytest

import food_calculator


def test_postive_example():
    assert food_calculator.calculate_food_order(5, 3, 7, 17) == 363.6


def test_leftover_food_float():
    assert food_calculator.calculate_food_order(5, 3, 7, 17.57) == 362.92


def test_no_leftover_food():
    assert food_calculator.calculate_food_order(5, 3, 7, 0) == 384.0


def test_no_medium_dogs():
    assert food_calculator.calculate_food_order(5, 0, 7, 10) == 300.0


def test_excess_leftover_food():
    assert food_calculator.calculate_food_order(5, 5, 7, 1000) == 0


def test_max_dogs():
    assert food_calculator.calculate_food_order(10, 10, 10, 0) == 720


# negative cases

def test_maximum_dogs_exceeded():
    with pytest.raises(ValueError, match="50 exceeds the maximum number \\(30\\) of dogs."):
        food_calculator.calculate_food_order(10, 10, 30, 20)


def test_partial_dog():
    with pytest.raises(TypeError, match="Invalid quantity of dogs \\(5.1\\) specified. You must enter an integer."):
        food_calculator.calculate_food_order(5.1, 3, 7, 17)


def test_negative_dog():
    with pytest.raises(TypeError, match="Negative dogs are not allowed. You must enter a positive integer."):
        food_calculator.calculate_food_order(-5, 3, 7, 17)


def test_invalid_dog():
    with pytest.raises(TypeError, match="Invalid quantity of dogs \\(Five\\) specified. You must enter an integer."):
        food_calculator.calculate_food_order('Five', 3, 7, 17)


def test_negative_food():
    with pytest.raises(TypeError, match="Negative leftover dog food is not allowed. You must enter a positive number."):
        food_calculator.calculate_food_order(5, 3, 7, -17)


def test_invalid_food():
    with pytest.raises(TypeError, match="Invalid quantity \\(Seventeen\\) of leftover food specified. You must enter "
                                        "a number."):
        food_calculator.calculate_food_order(5, 3, 7, 'Seventeen')


def test_zero_dogs():
    with pytest.raises(ValueError, match='You have no dogs and do not need to order food at this time.'):
        food_calculator.calculate_food_order(0, 0, 0, 10)
