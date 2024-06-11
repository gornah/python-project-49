import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(module):
    name = welcome_user()
    print(module.game_rule)
    count = 0
    game_round = 3
    while count < game_round:
        question, correct_answer = module.game()
        print(question)
        answer = input('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            count = 0
            return
    print(f'Congratulations, {name}!')
