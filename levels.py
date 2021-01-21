from random import randint


def one_plus_one():
    a = randint(2, 9)
    b = randint(2, 9)
    answer = a + b
    return a, b, "+", answer


def one_x_one():
    a = randint(2, 9)
    b = randint(2, 9)
    answer = a * b
    return a, b, "*", answer


def two_or_three_x_11():
    if randint(1, 2) == 1:
        a = randint(11, 99)
    else:
        a = randint(100, 999)
    b = 11
    answer = a * b
    return a, b, "*", answer


def square_5():
    """https://youtu.be/7wTLiUH6gn4?t=1448"""
    a = randint(1, 9) * 10 + 5
    answer = a * a
    return a, a, "*", answer


def two_x_two_same_tens_units_add_to_ten():
    """https://youtu.be/7wTLiUH6gn4?t=1563"""
    tens = randint(1, 9)
    unit = randint(1, 9)
    a = 10 * tens + unit
    b = 10 * tens + 10 - unit
    answer = a * b
    return a, b, "*", answer


def one_x_teen():
    """https://youtu.be/7wTLiUH6gn4?t=1725"""
    a = randint(11, 19)
    b = randint(2, 9)
    if randint(1,2) == 1:
        a,b = b,a
    answer = a * b
    return a, b, "*", answer


def teen_x_teen():
    """https://youtu.be/7wTLiUH6gn4?t=1857"""
    a = randint(10, 19)
    b = randint(10, 19)
    answer = a * b
    return a, b, "*", answer


def two_plus_two():
    """https://youtu.be/7wTLiUH6gn4?t=2288"""
    a = randint(10, 99)
    b = randint(10, 99)
    answer = a + b
    return a, b, "+", answer


def three_plus_three():
    """https://youtu.be/7wTLiUH6gn4?t=2456"""
    a = randint(10, 99)
    b = randint(10, 99)
    answer = a + b
    return a, b, "+", answer


def two_x_two():
    a = randint(10, 99)
    b = randint(10, 99)
    answer = a * b
    return a, b, "*", answer


levels = [
    one_plus_one,
    one_x_one,
    two_or_three_x_11,
    square_5,
    two_x_two_same_tens_units_add_to_ten,
    one_x_teen,
    teen_x_teen,
    two_plus_two,
    three_plus_three,
    # two_x_two,
]
