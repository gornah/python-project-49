#!/usr/bin/env python3
from random import randint
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        if answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def main():
    name = welcome_user()
    even_game(name)


if __name__ == '__main__':
    main()
