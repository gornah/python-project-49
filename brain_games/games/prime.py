from math import sqrt
from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    count = 2
    while count <= sqrt(num):
        if num % count == 0:
            return False
        count += 1
    return True


def game():
    num = randint(2, 21)
    question = (f'Question: {num}')
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question, correct_answer
