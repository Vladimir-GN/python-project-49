#!/usr/bin/env python3

import prompt
import random
import math


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Find the greatest common divisor of given numbers.')

    win_rounds = 0

    while win_rounds < 3:
  
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        gcd = math.gcd(number_1, number_2)

        print(f'Question: {number_1} {number_2}')
        print('Your answer: ', end='')
        user_answer = input()

        if int(user_answer) == gcd:
            print('Correct!')
            win_rounds += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{gcd}'.")
            break

    if win_rounds == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
