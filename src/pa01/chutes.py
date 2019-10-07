# -*- coding: utf-8 -*-

import random

__authors__ = 'Johan Stabekk, Sabina Langås'
__emails__ = 'johan.stabekk@nmbu.no, sabina.langaas@nmbu.no'


def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """
    ladders_and_snakes = {1: 40, 8: 10, 24: 5, 33: 3, 36: 52, 42: 30,
                          43: 62, 49: 79, 56: 37, 64: 27, 65: 82,
                          68: 85, 74: 12, 87: 70}
    max_roll = 6
    list_of_players = [0] * num_players
    positions = [0] * num_players
    highest_position = 0
    turns = 0

    while highest_position <= 90:
        turns += 1
        for player in list_of_players:
            roll = random.randint(1, max_roll)
            if positions[player] >= 90:
                break
            else:
                positions[player] += roll
                positions[player] = \
                    ladders_and_snakes.get(positions[player],
                                           positions[player])
        highest_position = max(positions)
    return turns


testrun = single_game(8)
print(testrun)


def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the number of moves needed in each game.
    """
    moves = [0] * num_games
    for game in range(num_games):
        moves[game] += single_game(num_players)

    pass


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the number of moves needed in each game.
    """
    pass
