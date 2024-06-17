from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    '''
    Check if a number is even.
    Return True if number is even, otherwise return False.
    '''
    if number % 2 == 0:
        return True
    else:
        return False


def game():
    '''
    Generate a question for the game and the correct answer.
    Return tuple which containing the question and the correct answer.
    '''
    number = randint(1, 100)
    question = (f'Question: {number}')
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
