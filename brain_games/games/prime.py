from math import sqrt
from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    '''
    Return True if number is prime, otherwise return False.
    '''
    count = 2
    while count <= sqrt(num):
        if num % count == 0:
            return False
        count += 1
    return True


def game():
    '''
    Generate a question for the game and the correct answer.
    Return tuple which containing the question and the correct answer.
    '''
    num = randint(2, 21)
    question = (f'Question: {num}')
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question, correct_answer
