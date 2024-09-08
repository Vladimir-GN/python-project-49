import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_round_data():
    start = random.randint(1, 100)
    step = random.randint(11, 31)
    length = 10
    hidden_index = random.randint(0, length - 1)
    progression_list = [start + i * step for i in range(length)]
    correct_answer = str(progression_list[hidden_index])
    progression_list[hidden_index] = ".."  # type: ignore
    question = f"{' '.join(map(str, progression_list))}"

    return question, correct_answer
