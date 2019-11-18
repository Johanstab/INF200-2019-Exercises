# -*- coding: utf-8 -*-

__author__ = 'Johan Stabekk, Sabina Langås'
__email__ = 'johansta@nmbu.no, sabinal@nmbu.no'

import chutes_simulation as cs
import pytest


def test_resilient_player_move():

    board = cs.Board()
    player = cs.ResilientPlayer(board)
    for _ in range(10):
        player.move()

    assert player.number_of_moves == 10


def test_resilient_player_position():

    board = cs.Board()
    player = cs.ResilientPlayer(board)
    start_pos = player.position
    player.move()
    end_pos = player.position

    assert start_pos is not end_pos


def test_resilient_player_position_not_equal_one():

    board = cs.Board()
    player = cs.ResilientPlayer(board)

    for _ in range(50):
        player.move()
        assert 1 < player.position



