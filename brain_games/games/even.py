from random import randint


# even game
def game():
    number = randint(1, 100)
    question = (f'Question: {number}')
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
