#!/usr/bin/env python3

from brain_games.game_engine import play_game
from brain_games.games import check_even


def main():
    play_game(check_even)


if __name__ == "__main__":
    main()
