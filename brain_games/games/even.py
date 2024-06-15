from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def game():
    number = randint(1, 100)
    question = (f'Question: {number}')
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
