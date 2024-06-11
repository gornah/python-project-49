#!/usr/bin/env python3
from brain_games.engine import welcome_user, run_game
from brain_games.games.prime import game_prime, game_rule


def main():
    name = welcome_user()
    print(game_rule)
    run_game(game_prime, name)


if __name__ == '__main__':
    main()
