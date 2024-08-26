#!/usr/bin/env python3

import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')

    win_rounds = 0

    while win_rounds < 3:

        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        operator = random.choice(('+-*'))
        question = f'{number_1} {operator} {number_2}'

        if operator == '+':
            calculate = number_1 + number_2
        elif operator == '-':
            calculate = number_1 - number_2
        elif operator == '*':
            calculate = number_1 * number_2

        print(f'Question: {question}')
        print('Your answer: ', end='')
        user_answer = input()

        if int(user_answer) == calculate:
            print('Correct!')
            win_rounds += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{calculate}'.")
            break

    if win_rounds == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
