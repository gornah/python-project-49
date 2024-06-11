from random import randint
from random import choice


def game_calc():
    x = randint(5, 10)
    y = randint(1, 5)
    operation = choice(['+', '-', '*'])
    question = (f'Question: {x} {operation} {y}')
    correct_answer = eval(f'{x} {operation} {y}')
    return question, correct_answer


game_rule = 'What is the result of the expression?'
