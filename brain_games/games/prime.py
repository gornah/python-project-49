from math import sqrt
from random import randint


def is_prime(num):
    count = 2
    while count <= sqrt(num):
        if num % count == 0:
            return False
        count += 1
    return True


# prime game
def game():
    num = randint(2, 21)
    question = (f'Question: {num}')
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question, correct_answer


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
