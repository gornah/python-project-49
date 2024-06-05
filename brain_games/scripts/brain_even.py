#!/usr/bin/env python3
from brain_games.games.engine import welcome_user, run_game
from brain_games.games.brain_even import even_game, game_rule


def main():
    name = welcome_user()
    print(game_rule)
    run_game(even_game, name)


if __name__ == '__main__':
    main()
