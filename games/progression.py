import random
from games.greeting import greeting


def play_game():
    name = greeting()
    print('What number is missing in the progression?')

    rounds = 3

    for _ in range(rounds):
        start = random.randint(1, 100)
        step = random.randint(11, 31)
        length = 10
        progression_list = []

        for i in range(length):
            progression_list.append(start + i * step)

        hidden_index = random.randint(0, length - 1)
        correct_answer = progression_list[hidden_index]
        progression_list[hidden_index] = ".."

        print(f"Question: {' '.join(map(str, progression_list))}")
        answer = int(input("Your answer: "))

        if int(answer) == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. '"
                  f"'Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
