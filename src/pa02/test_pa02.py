# -*- coding: utf-8 -*-

import chutes_simulation as cs
import pytest

__author__ = 'Johan Stabekk, Sabina Langås'
__email__ = 'johansta@nmbu.no, sabinal@nmbu.no'


class TestPlayer:
    def test_move(self):

        board = cs.Board()
        player = cs.Player(board)
        for _ in range(10):
            player.move()

        assert player.number_of_moves == 10

    def test_position(self):

        board = cs.Board()
        player = cs.Player(board)
        start_pos = player.position
        player.move()
        end_pos = player.position

        assert start_pos is not end_pos

    def test_position_not_equal_one(self):

        board = cs.Board()
        player = cs.Player(board)

        for _ in range(50):
            player.move()
            assert 1 <= player.position

    def test_start_of_chute(self):

        board = cs.Board()
        player = cs.ResilientPlayer(board)

        for step in range(50):
            player.move()
            assert player.position not in board.snakes_and_ladders.keys()


class TestLazyPlayer:
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
