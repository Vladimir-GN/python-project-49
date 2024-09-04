import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    count = 0

    for i in range(2, number):
        if number % i == 0:
            count += 1
    if count <= 0:
        return True
    else:
        return False


def condition_task():
    number = random.randint(2, 100)
    question = f'{number}'
    correct_answer = 'yes' if is_prime(number) else 'no'

    return question, correct_answer
