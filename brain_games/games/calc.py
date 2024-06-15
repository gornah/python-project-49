from random import randint
from random import choice

GAME_RULE = 'What is the result of the expression?'


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
}


def game():
    x = randint(5, 10)
    y = randint(1, 5)
    operation = choice(['+', '-', '*'])
    question = (f'Question: {x} {operation} {y}')
    correct_answer = operations[operation](x, y)
    return question, correct_answer
