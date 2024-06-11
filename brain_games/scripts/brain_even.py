#!/usr/bin/env python3
from brain_games.engine import welcome_user, run_game
from brain_games.games.brain_even import game_even, game_rule


def main():
    name = welcome_user()
    print(game_rule)
    run_game(game_even, name)


if __name__ == '__main__':
    main()
