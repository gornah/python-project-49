from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def gcd(x, y):
    '''
    Return the greatest common divisor of two numbers.
    '''
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y


def game():
    '''
    Generate a question for the game and the correct answer.
    Return tuple which containing the question and the correct answer.
    '''
    x = randint(1, 50)
    y = randint(1, 50)
    question = (f'Question: {x} {y}')
    correct_answer = gcd(x, y)
    return question, correct_answer
