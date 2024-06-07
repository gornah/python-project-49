from random import randint


def game_even():
    number = randint(1, 100)
    question = (f'Question: {number}')
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer


game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
