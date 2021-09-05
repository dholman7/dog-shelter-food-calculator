s_need = 10
m_need = 20
l_need = 30
max_dogs = 30
food_multiplier = 1.2


def calculate_food_order(small, medium, large, leftover_food):
    """
    Calculates the amount of food to order
    :param small: number of small dogs
    :param medium: number of medium dogs
    :param large: number of large dogs
    :param leftover_food: amount of leftover food
    :return: order_amount: The amount of food to order
    """
    check_input([small, medium, large])
    check_leftover(leftover_food)
    total_dogs = small + medium + large
    check_total_dogs(total_dogs)
    needed_amount = small * s_need + medium * m_need + large * l_need
    order_amount = round((needed_amount - leftover_food) * food_multiplier, 2)
    order_amount = check_order_amount(order_amount)
    print(f"You need to order {str(order_amount)} lbs of dog food.")
    return order_amount


def check_input(value):
    for vals in value:
        if type(vals) != int:
            raise TypeError(f"Invalid quantity of dogs ({str(vals)}) specified. You must enter an integer.")
        if vals < 0:
            raise TypeError("Negative dogs are not allowed. You must enter a positive integer.")


def check_leftover(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Invalid quantity ({str(value)}) of leftover food specified. You must enter a number.")
    if value < 0:
        raise TypeError("Negative leftover dog food is not allowed. You must enter a positive number.")


def check_total_dogs(total):
    if total > max_dogs:
        raise ValueError(f"{total} exceeds the maximum number ({max_dogs}) of dogs.")
    if total == 0:
        raise ValueError('You have no dogs and do not need to order food at this time.')


def check_order_amount(order_amount):
    if order_amount < 0:
        print('You have an excesss amount of dog food.')
        return 0
    else:
        return order_amount


if __name__ == '__main__':
    sml = int(input('Enter total number of small dogs: '))
    med = int(input('Enter total number of medium dogs: '))
    lrg = int(input('Enter total number of large dogs: '))
    left = int(input('Enter total amount of leftover food: '))

    calculate_food_order(sml, med, lrg, left)
