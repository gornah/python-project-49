from random import randint

GAME_RULE = 'What number is missing in the progression?'


def generate_progression():
    '''
    Generate a random arithmetic progression.
    Return a list of integers representing the arithmetic progression.
    '''
    start = randint(1, 10)
    step = randint(1, 10)
    length = randint(5, 10)
    progression_list = [start + step * i for i in range(length)]
    return progression_list


def game():
    '''
    Generate a question for the game and the correct answer.
    Return tuple which containing the question and the correct answer.
    '''
    progression = generate_progression()
    index = randint(0, len(progression) - 1)
    correct_answer = progression.pop(index)
    progression.insert(index, '..')
    question = 'Question: ' + ' '.join(map(str, progression))
    return question, correct_answer
