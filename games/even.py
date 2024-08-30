import random
from games.greeting import greeting


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def play_game():
    name = greeting()
    print('What is the result of the expression?')

    rounds = 3

    for _ in range(rounds):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ')
        correct_answer = 'yes' if is_even(number) else 'no'

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
