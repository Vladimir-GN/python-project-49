import random
import math
from games.greeting import greeting


def play_game():
    name = greeting()
    print('Find the greatest common divisor of given numbers.')

    rounds = 3

    for _ in range(rounds):
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        print(f'Question: {number_1} {number_2}')
        answer = input('Your answer: ')
        correct_answer = math.gcd(number_1, number_2)

        if int(answer) == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
