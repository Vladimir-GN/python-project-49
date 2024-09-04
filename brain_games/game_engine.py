import prompt
from brain_games.games.constants import ROUNDS_COUNT


def play_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'"Hello, {name}!')

    print(game.DESCRIPTION)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.condition_task()
        print('Question:', question)
        answer = input('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. '"
                  f"'Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
