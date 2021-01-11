from random import randint


def add_one_digit():
    """multiply <10"""
    a = randint(2, 9)
    b = randint(2, 9)
    answer = str(a + b)
    return a, b, "+", answer


def add_two_digit():
    """multiply <10"""
    a = randint(10, 99)
    b = randint(10, 99)
    answer = str(a + b)
    return a, b, "+", answer


def mul_one_digit():
    """multiply <10"""
    a = randint(2, 9)
    b = randint(2, 9)
    answer = str(a * b)
    return a, b, "*", answer


def mul_two_digit():
    """multiply <10"""
    a = randint(10, 99)
    b = randint(10, 99)
    answer = str(a * b)
    return a, b, "*", answer


levels = [add_one_digit, mul_one_digit, add_two_digit, mul_two_digit]