import random
from games.greeting import greeting


def is_prime(n):
    if n <= 1 or (n > 3 and (n % 2 == 0 or n % 3 == 0)):
        return False
    for i in range(5, int(n**0.5) + 1, 2):
        if n % i == 0:
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
        correct_answer = 'yes' if is_prime(number) else 'no'
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. '"
                  f"'Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
