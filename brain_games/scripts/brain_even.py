#!/usr/bin/env python3

import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no"')

    count = 0

    while count < 3:

        question_number = random.randint(1, 100)

        if question_number % 2 == 0:
            correct = 'yes'
        else:
            correct = 'no'

        print(f'Question: {question_number}')
        print('Your answer: ', end='')
        answer = input()

        if answer == correct:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            break

    if count == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
