from random import randint


def gcd(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y


def game_gcd():
    x = randint(1, 50)
    y = randint(1, 50)
    question = (f'Question: {x} {y}')
    correct_answer = gcd(x, y)
    return question, correct_answer


game_rule = 'Find the greatest common divisor of given numbers.'
