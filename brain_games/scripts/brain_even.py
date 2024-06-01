#!/usr/bin/env python3
from random import randint
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer == 'yes':
            print('Correct!')
            count += 1
        elif number % 2 != 0 and answer == 'no':
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            return


def main():
    welcome_user()
    even_game()


if __name__ == '__main__':
    main()
