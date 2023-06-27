import unittest
from main import Player


class TestPlayer(unittest.TestCase):
    def test_minimum(self):
        pl = Player(True, 1000, 6, 1)
        pl.throw_dice()
        self.assertGreaterEqual(pl.dice, 1)

    def test_maximum(self):
        pl = Player(True, 1000, 6, 1)
        pl.throw_dice()
        self.assertLessEqual(pl.dice, 6)

    def test_bet(self):
        pl = Player(False, 1000, 6, 1)
        pl.bet(100)
        self.assertEqual(pl.bet_amount, 100)

    def test_win(self):
        pl = Player(False, 1000, 6, 1)
        pl.bet(1000)
        pl.win(1100)
        self.assertEqual(1100, pl.bank )
        self.assertEqual(1, pl.wins)
        self.assertEqual(0, pl.bet_amount)

    def test_lose(self):
        pl = Player(False, 1000, 6, 1)
        pl.bet(1000)
        pl.lose()
        self.assertEqual(0, pl.bank)
        self.assertEqual(0, pl.wins)
        self.assertEqual(0, pl.bet_amount)



if __name__ == '__main__':
    unittest.main()
