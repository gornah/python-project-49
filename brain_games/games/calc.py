from random import randint
from random import choice

GAME_RULE = 'What is the result of the expression?'


def add(a, b):
    '''
    Return the sum of two numbers.
    '''
    return a + b


def subtract(a, b):
    '''
    Return the subtract one number from another.
    '''
    return a - b


def multiply(a, b):
    '''
    Return the multiply of two numbers.
    '''
    return a * b


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
}


def game():
    '''
    Generate a question for the game and the correct answer.
    Return tuple which containing the question and the correct answer.
    '''
    x = randint(5, 10)
    y = randint(1, 5)
    operation = choice(['+', '-', '*'])
    question = (f'Question: {x} {operation} {y}')
    correct_answer = operations[operation](x, y)
    return question, correct_answer
