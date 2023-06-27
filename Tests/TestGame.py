import unittest
from main import Game


class TestGame(unittest.TestCase):
    def test_create_players(self):
        game = Game(5, 1000, 3, 6, 1)
        self.assertEqual(5, len(game.players))

    def test_throw_dices(self):
        game = Game(5, 1000, 3, 6, 1, only_cpu=True)
        game.throw_dices()
        for player in game.players:
            self.assertIsNotNone(player.dice)

    def test_calculate_scores(self):
        game = Game(5, 1000, 100, 6, 1, only_cpu=True)
        game.throw_dices()
        game.calculate_scores()
        winning_dice = max([player.dice for player in game.players])
        for player in game.players:
            if player.wins == 1:
                test_player = player
                break
        self.assertEqual(winning_dice, test_player.dice)


if __name__ == '__main__':
    unittest.main()
