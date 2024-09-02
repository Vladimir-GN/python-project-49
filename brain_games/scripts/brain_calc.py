#!/usr/bin/env python3

from brain_games.game_engine import play_game
from brain_games.games import calculate


def main():
    play_game(calculate)


if __name__ == "__main__":
    main()
