import unittest
from Bowling import Bowling

class TestBowling(unittest.TestCase):
    def setUp(self):
        self.game = Bowling()

    def roll_many(self, n, pins):
        for _ in range(n):
            self.game.roll(pins)

    def test_all_gutter_balls(self):
        self.roll_many(20, 0)
        self.assertEqual(self.game.get_score(), 0)

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(self.game.get_score(), 20)

    def test_all_zeros(self):
        self.roll_many(20, 0)
        self.assertEqual(self.game.get_score(), 0)

    def test_all_spares(self):
        self.roll_many(21, 5)
        self.assertEqual(self.game.get_score(), 150)

    def test_all_strikes(self):
        self.roll_many(12, 10)
        self.assertEqual(self.game.get_score(), 300)

    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)  # spare
        self.game.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(self.game.get_score(), 16)

    def test_one_strike(self):
        self.game.roll(10)  # strike
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(self.game.get_score(), 24)

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(self.game.get_score(), 300)

    def test_invalid_roll(self):
        with self.assertRaises(ValueError):
            self.game.roll(11)

    def test_get_frameScore(self):
        self.game.roll(10)  # Frame 1
        self.game.roll(9)   # Frame 2
        self.game.roll(1)   # Frame 2 (spare)
        self.game.roll(5)   # Frame 3
        self.game.roll(5)   # Frame 3 (spare)
        self.game.roll(7)   # Frame 4
        self.game.roll(2)   # Frame 4
        self.roll_many(12, 0)  # Remaining frames

        self.assertEqual(self.game.get_frameScore(1), 20)
        self.assertEqual(self.game.get_frameScore(2), 35)
        self.assertEqual(self.game.get_frameScore(3), 52)
        self.assertEqual(self.game.get_frameScore(4), 61)
