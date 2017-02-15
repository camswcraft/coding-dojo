import unittest
import rock_paper_scissors as game
from rock_paper_scissors import SCISSORS, PAPER, ROCK


class TestRockPaperScissors(unittest.TestCase):
    def test_rock_beats_scissors(self):
        p1 = game.Player(ROCK)
        p2 = game.Player(SCISSORS)
        result = game.round(p1, p2)
        self.assertEquals(game.P1_WIN, result)

    def test_scissors_ties_with_scissors(self):
        p1 = game.Player(SCISSORS)
        p2 = game.Player(SCISSORS)
        result = game.round(p1, p2)
        self.assertEquals(game.DRAW, result)

    def test_scissors_beats_paper(self):
        result = game.round(SCISSORS, PAPER)
        self.assertEquals(game.P1_WIN, result)

    def test_paper_beats_rock(self):
        result = game.round(PAPER, ROCK)
        self.assertEquals(game.P1_WIN, result)

    def test_rock_loses_to_paper(self):
        result = game.round(ROCK, PAPER)
        self.assertEquals(game.P2_WIN, result)

    def test_paper_loses_to_scissors(self):
        result = game.round(PAPER, SCISSORS)
        self.assertEquals(game.P2_WIN, result)

    def test_scissors_loses_to_rock(self):
        result = game.round(SCISSORS, ROCK)
        self.assertEquals(game.P2_WIN, result)