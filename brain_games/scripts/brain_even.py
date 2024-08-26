#!/usr/bin/env python3

import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no"')

    correct_answer = 0

    while correct_answer < 3:

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
            correct_answer += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{even}'.")
            break

    if correct_answer == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
