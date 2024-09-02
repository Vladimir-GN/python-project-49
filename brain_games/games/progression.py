import random

DESCRIPTION = 'What number is missing in the progression?'


def task():
    start = random.randint(1, 100)
    step = random.randint(11, 31)
    length = 10
    progression_list = []

    for i in range(length):
        progression_list.append(start + i * step)
        hidden_index = random.randint(0, length - 1)

    correct_answer = str(progression_list[hidden_index])
    progression_list[hidden_index] = ".."
    question = f"{' '.join(map(str, progression_list))}"

    return question, correct_answer
