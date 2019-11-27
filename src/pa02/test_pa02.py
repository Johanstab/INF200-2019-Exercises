# -*- coding: utf-8 -*-

import chutes_simulation as cs
import pytest

__author__ = 'Johan Stabekk, Sabina Langås'
__email__ = 'johansta@nmbu.no, sabinal@nmbu.no'


class TestPlayer:
    """Tests for Player class"""

    def test_move(self):
        """Tests if the players in Player Class takes the right amounts of
        moves"""

        board = cs.Board()
        player = cs.Player(board)
        for _ in range(10):
            player.move()

        assert player.number_of_moves == 10

    def test_position(self):
        """Tests that the player actually moves, when function move is
        called upon. So start position can not be equal to end position  """

        board = cs.Board()
        player = cs.Player(board)
        start_pos = player.position
        player.move()
        end_pos = player.position

        assert start_pos is not end_pos

    def test_position_not_equal_one(self):
        """Test that the players position is not less than 1 after moving,
        since this is not possible"""

        board = cs.Board()
        player = cs.Player(board)

        for _ in range(50):
            player.move()
            assert 1 <= player.position

    def test_start_of_chute(self):
        """Test that the players position can´t be the start point of a
        snake or a ladder, since the player is supposed to interact with
        these. """

        board = cs.Board()
        player = cs.ResilientPlayer(board)

        for step in range(50):
            player.move()
            assert player.position not in board.snakes_and_ladders.keys()


class TestLazyPlayer:
    """Tests for LazyPlayer class
    The following test, has the same function as those in Player class. The
    only different is that the test for LazyPlayer. Therefore the follow the
    same docstrings as in Player class, and I will not be repeated"""

    def test_move(self):

        board = cs.Board()
        player = cs.LazyPlayer(board)
        for _ in range(10):
            player.move()

        assert player.number_of_moves == 10

    def test_position(self):

        board = cs.Board()
        player = cs.LazyPlayer(board)
        start_pos = player.position
        player.move()
        end_pos = player.position

        assert start_pos is not end_pos

    def test_position_not_equal_one(self):

        board = cs.Board()
        player = cs.LazyPlayer(board)

        for _ in range(50):
            player.move()
            assert 1 <= player.position

    def test_start_of_chute(self):

        board = cs.Board()
        player = cs.ResilientPlayer(board)

        for step in range(50):
            player.move()
            assert player.position not in board.snakes_and_ladders.keys()


class TestResilientPlayer:
    """Tests for ResilientPlayer class
    The following test, has the same function as those in Player class. The
    only different is that the test for ResilientPlayer. Therefore the
    follow the same docstrings as in Player class, and I will not be
    repeated"""

    def test_move(self):

        board = cs.Board()
        player = cs.ResilientPlayer(board)
        for _ in range(10):
            player.move()

        assert player.number_of_moves == 10

    def test_position(self):

        board = cs.Board()
        player = cs.ResilientPlayer(board)
        start_pos = player.position
        player.move()
        end_pos = player.position

        assert start_pos is not end_pos

    def test_position_not_equal_one(self):

        board = cs.Board()
        player = cs.ResilientPlayer(board)

        for _ in range(50):
            player.move()
            assert 1 <= player.position

    def test_start_of_chute(self):

        board = cs.Board()
        player = cs.ResilientPlayer(board)

        for step in range(50):
            player.move()
            assert player.position not in board.snakes_and_ladders.keys()


class TestSimulation:
    """Test for Simulation class"""

    def test_simulations_players_per_type(self):
        """Test if players_per_type returns the right kind of value"""

        sim = cs.Simulation([cs.Player, cs.Player, cs.LazyPlayer,
                             cs.LazyPlayer, cs.ResilientPlayer,
                             cs.ResilientPlayer], randomize_players=False)

        sim.run_simulation(5)

        assert sim.players_per_type() == {'ResilientPlayer': 2,
                                          'LazyPlayer': 2, 'Player': 2}

    def test_simulations_single_game(self):
        """Test if single_game returns the right kind of value"""

        sim = cs.Simulation([cs.Player, cs.Player, cs.LazyPlayer,
                             cs.LazyPlayer, cs.ResilientPlayer,
                             cs.ResilientPlayer], randomize_players=False)
        run = sim.single_game()

        assert run == (15, 'LazyPlayer')

    def test_simulations_get_results(self):
        """Test if get_results returns right kind of value"""

        sim = cs.Simulation([cs.Player, cs.Player, cs.LazyPlayer,
                             cs.LazyPlayer, cs.ResilientPlayer,
                             cs.ResilientPlayer], randomize_players=False)

        sim.run_simulation(5)

        results = sim.get_results()

        assert results == [(15, 'LazyPlayer'), (6, 'LazyPlayer'),
                           (21, 'ResilientPlayer'), (13, 'Player'),
                           (5, 'Player')]

    def test_simulations_durations_per_type(self):
        """Test if durations_per_type returns the right value"""

        sim = cs.Simulation([cs.Player, cs.Player, cs.LazyPlayer,
                             cs.LazyPlayer, cs.ResilientPlayer,
                             cs.ResilientPlayer], randomize_players=False)

        sim.run_simulation(5)

        durations = sim.durations_per_type()

        assert durations == {'Player': [13, 5], 'ResilientPlayer': [21],
                             'LazyPlayer': [15, 6]}
