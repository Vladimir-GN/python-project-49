import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 2:
        return True
    if number == 1 or number % 2 == 0:
        return False
    limit = int(number ** 0.5) + 1
    for i in range(3, limit, 2):
        if number % i == 0:
            return False
    return True


def task():
    number = random.randint(1, 100)
    question = f'{number}'
    correct_answer = 'yes' if is_prime(number) else 'no'

    return question, correct_answer
