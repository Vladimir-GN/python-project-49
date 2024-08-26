import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print("What number is missing in the progression?")

    win_rounds = 0

    while win_rounds < 3:
        start = random.randint(1, 50)
        step = random.randint(1, 9)
        length = 10
        progression_list = []

        for i in range(length):
            progression_list.append(start + i * step)

        hidden_index = random.randint(0, length - 1)
        correct_answer = progression_list[hidden_index]
        progression_list[hidden_index] = ".."

        print(f"Question: {' '.join(map(str, progression_list))}")
        user_answer = int(input("Your answer: "))

        if int(user_answer) == correct_answer:
            print('Correct!')
            win_rounds += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break

    if win_rounds == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
