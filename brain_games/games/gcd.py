import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def condition_task():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    correct_answer = str(math.gcd(number_1, number_2))
    question = f'{number_1} {number_2}'

    return question, correct_answer
