import random
from games.greeting import greeting


def simple(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number / 0.5), 2):
        if number % i == 0:
            return False
    return True


def play_game():
    name = greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    rounds = 3

    for _ in range(rounds):
        number = random.randint(1, 100)
        
        print(f'Question: {number}')
        answer = input('Your answer: ')
        correct_answer = 'yes' if simple(number) else 'no'
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
