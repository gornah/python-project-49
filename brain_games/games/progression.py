from random import randint

GAME_RULE = 'What number is missing in the progression?'


def generate_progression():
    start = randint(1, 10)
    step = randint(1, 10)
    length = randint(5, 10)
    progression_list = [start + step * i for i in range(length)]
    return progression_list


def game():
    progression = generate_progression()
    index = randint(0, len(progression) - 1)
    correct_answer = progression.pop(index)
    progression.insert(index, '..')
    question = 'Question: ' + ' '.join(map(str, progression))
    return question, correct_answer
