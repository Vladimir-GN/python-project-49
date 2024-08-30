import random
from games.greeting import greeting


def is_calc(number_1, number_2, operator):
    if operator == '+':
        calculate = number_1 + number_2
    elif operator == '-':
        calculate = number_1 - number_2
    elif operator == '*':
        calculate = number_1 * number_2
    return calculate


def play_game():
    name = greeting()
    print('What is the result of the expression?')

    rounds = 3

    for _ in range(rounds):
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 50)
        operator = random.choice('+-*')

        print(f'Question: {number_1} {operator} {number_2}')
        answer = input('Your answer: ')
        correct_answer = is_calc(number_1, number_2, operator)

        if int(answer) == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
