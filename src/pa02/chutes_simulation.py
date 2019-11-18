# -*- coding: utf-8 -*-

import random

__author__ = 'Johan Stabekk, Sabina Langås'
__email__ = 'johansta@nmbu.no, sabinal@nmbu.no'


class Board:
    snakes = [
              (1, 40), (8, 10), (36, 52), (43, 62),
              (49, 79), (65, 82), (68, 85)
              ]
    ladders = [
               (24, 5), (33, 3), (42, 30), (56, 37),
               (64, 27), (74, 12), (87, 70)
               ]
    goal = 90

    def __init__(self, snakes=None, ladders=None, goal=None):
        """

        Parameters
        ----------
        snakes
        ladders
        goal
        """
        if ladders is None:
            ladders = Board.ladders
        if snakes is None:
            snakes = Board.snakes

        if goal is None:
            self.goal = Board.goal
        else:
            self.goal = goal

        self.snakes_and_ladders = {start: end for start,
                                   end in snakes + ladders}

    def goal_reached(self, position):
        """

        Parameters
        ----------
        position

        Returns
        -------

        """
        return position >= self.goal

    def position_adjustment(self, position):
        """

        Parameters
        ----------
        position

        Returns
        -------

        """
        new_position = self.snakes_and_ladders.get(position, position)

        return new_position - position


class Player:

    def __init__(self, board):
        """

        Parameters
        ----------
        board
        """
        self.board = board
        self.position = 0
        self.number_of_moves = 0

    def move(self):
        """

        Returns
        -------

        """
        roll = random.randint(1, 6)

        self.position += roll
        self.position += self.board.position_adjustment(self.position)
        self.number_of_moves += 1


class ResilientPlayer(Player):

    def __init__(self, board, extra_steps=1):
        """

        Parameters
        ----------
        board
        extra_steps
        """
        super().__init__(board)
        self.plus_step = extra_steps
        self.fell_down = False

    def move(self):
        """

        Returns
        -------

        """
        if self.fell_down:
            extra = self.plus_step
        else:
            extra = 0

        roll = random.randint(1, 6)

        self.position += roll + extra
        self.position += self.board.position_adjustment(self.position)
        self.number_of_moves += 1


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=1):
        """

        Parameters
        ----------
        board
        dropped_steps
        """
        super().__init__(board)
        self.minus_step = dropped_steps
        self.climbed = False

    def move(self):
        """

        Returns
        -------

        """
        if self.climbed:
            extra = self.minus_step
        else:
            extra = 0

        roll = random.randint(1, 6)

        self.position += roll + extra
        self.position += self.board.position_adjustment(self.position)
        self.number_of_moves += 1


class Simulation:
    def __init__(self, player_field, board=None,
                 seed=1, randomize_players=False,
                 ):
        """

        Parameters
        ----------
        player_field
        board
        seed
        randomize_players
        """
        if board is None:
            self.board = Board()
        else:
            self.board = board

        self.player_types = frozenset(c.__name__ for c in player_field)
        self.players = player_field
        self.seed = random.seed(seed)
        self.randomize_players = randomize_players
        self.results = []

        if self.randomize_players:
            random.shuffle(self.players)

    def single_game(self):
        """

        Returns
        -------

        """
        players = [player(self.board) for player in self.players]
        while True:
            for player in players:
                player.move()
                if self.board.goal_reached(player.position):
                    return player.number_of_moves, type(player).__name__

    def run_simulation(self, number_of_games):
        """

        Parameters
        ----------
        number_of_games

        Returns
        -------

        """
        for _ in range(number_of_games):
            self.results.append(self.single_game())

    def get_results(self):
        """

        Returns
        -------

        """
        return self.results

    def winners_per_type(self):
        """

        Returns
        -------

        """
        winners_type = list(zip(*self.results))[1]

        winners_type_dict = {player_type: winners_type.count(player_type)
                             for player_type in self.player_types}

        return winners_type_dict

    def durations_per_type(self):
        """

        Returns
        -------

        """
        return {player_type: [duration for duration, p_type in self.results if
                              p_type == player_type] for player_type in
                self.player_types}

    def players_per_type(self):
        """

        Returns
        -------

        """
        players_dic = {}

        for player_type in frozenset(self.players):
            players_dic.update({
                player_type.__name__: self.players.count(player_type)})

        return players_dic


if __name__ == '__main__':

    sim = Simulation([Player, Player, LazyPlayer, ResilientPlayer])
    print(sim.single_game())

    sim.run_simulation(5)
    print(sim.players_per_type())


