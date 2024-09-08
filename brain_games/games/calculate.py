import random

DESCRIPTION = 'What is the result of the expression?'


def generate_round_data():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 50)
    operator = random.choice('+-*')
    question = f'{number_1} {operator} {number_2}'

    if operator == '+':
        correct_answer = str(number_1 + number_2)
    elif operator == '-':
        correct_answer = str(number_1 - number_2)
    elif operator == '*':
        correct_answer = str(number_1 * number_2)

    return question, correct_answer
