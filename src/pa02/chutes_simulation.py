# -*- coding: utf-8 -*-

import random

__author__ = 'Johan Stabekk, Sabina Langås'
__email__ = 'johansta@nmbu.no, sabinal@nmbu.no'


class Board:
    """
    This class represents the game board og 90 squares.
    """
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
        """This function generates the board that going to be used in the
        game of snakes and ladders.

        Parameters
        ----------
        snakes: The "snakes" that should be used in the board. If none is
                given, we use default "snakes". Snakes make the player go down.

        ladders: The "ladders" that should be used in the board. If none is
                given, we use default "ladders". Ladders make player go up.

        goal: The value that the player needs to reach to win the game. The
            game stops after o ne player reaches goal.
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
        position: The current position of the player

        Returns: Returns True if the position of the player have reached
                goal or passed goal
        -------
        True if position is greater than end destination(goal)
        """
        return position >= self.goal

    def position_adjustment(self, position):
        """
        Adjusts the position due to snakes and ladders.
        If the player is not at a start square for snakes or ladders,
        then it returns 0.

        Parameters
        ----------
        position: The current position of the player

        Returns
        -------
        The new position according to the snakes and ladders
        """
        new_position = self.snakes_and_ladders.get(position, position)

        return new_position - position


class Player:
    """
    Sets up a single player.
    """
    def __init__(self, board):
        """
        Parameters
        ----------
        board : The board that the player is on
        """
        self.board = board
        self.position = 0
        self.number_of_moves = 0

    def move(self):
        """
        Moves the player to a new position
        """
        roll = random.randint(1, 6)

        self.position += roll
        self.position += self.board.position_adjustment(self.position)
        self.number_of_moves += 1


class ResilientPlayer(Player):
    """
    Implements a player that is more resilient.
    This player will take x extra steps after falling down a chute.
    """
    def __init__(self, board, extra_steps=1):
        """
        Parameters
        ----------
        extra_steps : The number of extra steps taken after falling down a
        snake.
        """
        super().__init__(board)
        self.plus_step = extra_steps
        self.fell_down = False

    def move(self):
        if self.fell_down:
            extra = self.plus_step
        else:
            extra = 0

        roll = random.randint(1, 6)

        self.position += roll + extra
        self.position += self.board.position_adjustment(self.position)
        self.number_of_moves += 1


class LazyPlayer(Player):
    """
    Implements a lazy player that will drop down x steps after
    climbing a ladder. This will happen in the next round.
    """
    def __init__(self, board, dropped_steps=1):
        """
        Parameters
        ----------
        dropped_steps : The number of steps dropped after climbing a ladder
        """
        super().__init__(board)
        self.minus_step = dropped_steps
        self.climbed = False

    def move(self):
        if self.climbed:
            extra = self.minus_step
        else:
            extra = 0

        roll = random.randint(1, 6)

        self.position += roll + extra
        self.position += self.board.position_adjustment(self.position)
        self.number_of_moves += 1


class Simulation:
    """
    Sets up a full snakes and ladders simulation
    """
    def __init__(self, player_field, board=None,
                 seed=1, randomize_players=False,
                 ):
        """
        Parameters
        ----------
        player_field : A list of the player classes
        board: The Board they play on (Defaults as a standard board)
        seed: Random seed generator
        randomize_players: If the players should be in randomized order
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

        if self.randomize_players is True:
            random.shuffle(self.players)

    def single_game(self):
        """ Returns the winner type and number of moves for a single game

        Returns
        -------
        A tuple with (number_of_moves, winner_type)
        """
        players = [player(self.board) for player in self.players]
        while True:
            for player in players:
                player.move()
                if self.board.goal_reached(player.position):
                    return player.number_of_moves, type(player).__name__

    def run_simulation(self, number_of_games):
        """ Runs a given set of games. The results are stored in
            the Simulation class.

        Parameters
        ----------
        number_of_games: The number of games that should be played
        """
        for _ in range(number_of_games):
            self.results.append(self.single_game())

    def get_results(self):
        """
        Returns
        -------
        The results stored in Simulation.
        """
        return self.results

    def winners_per_type(self):
        """
        Returns
        -------
        A dictionary of the number of winners per type
        """
        winners_type = list(zip(*self.results))[1]

        winners_type_dict = {player_type: winners_type.count(player_type)
                             for player_type in self.player_types}

        return winners_type_dict

    def durations_per_type(self):
        """
        Returns
        -------
        A dictionary containing the game duration per player type
        """
        return {player_type: [duration for duration, p_type in self.results if
                              p_type == player_type] for player_type in
                self.player_types}

    def players_per_type(self):
        """
        Returns
        -------
        A dictionary showing how many players of each type
        """
        players_dic = {}

        for player_type in frozenset(self.players):
            players_dic.update({
                player_type.__name__: self.players.count(player_type)})

        return players_dic


if __name__ == '__main__':

    print(f'Simulation: Normal board, 6 players')
    sim = Simulation([Player, Player, LazyPlayer, LazyPlayer,
                      ResilientPlayer, ResilientPlayer],
                     randomize_players=False)

    sim.run_simulation(5)
    print(sim.durations_per_type())
    print(sim.get_results())
    print(sim.players_per_type())
