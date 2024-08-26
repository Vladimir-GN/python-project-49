#!/usr/bin/env python3

import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no"')

    win_rounds = 0

    while win_rounds < 3:

        question_number = random.randint(1, 100)

        if question_number % 2 == 0:
            even = 'yes'
        else:
            even = 'no'

        print(f'Question: {question_number}')
        print('Your answer: ', end='')
        user_answer = input()

        if user_answer == even:
            print('Correct!')
            win_rounds += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{even}'.")
            break

    if win_rounds == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
