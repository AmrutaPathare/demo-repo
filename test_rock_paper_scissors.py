import unittest
from rock_paper_scissors import RockPaperScissors

class DummyRoot:
    def __init__(self):
        self.title_called = False
    def title(self, text):
        self.title_called = True

class TestRockPaperScissors(unittest.TestCase):
    def setUp(self):
        self.app = RockPaperScissors(DummyRoot())

    def test_draw(self):
        for choice in self.app.choices:
            self.app.player_score = 0
            self.app.computer_score = 0
            result = self.app.get_result(choice, choice)
            self.assertEqual(result, "Draw")
            self.assertEqual(self.app.player_score, 0)
            self.assertEqual(self.app.computer_score, 0)

    def test_player_wins(self):
        wins = [('Rock', 'Scissors'), ('Paper', 'Rock'), ('Scissors', 'Paper')]
        for player, computer in wins:
            self.app.player_score = 0
            self.app.computer_score = 0
            result = self.app.get_result(player, computer)
            self.assertEqual(result, "You Win")
            self.assertEqual(self.app.player_score, 1)
            self.assertEqual(self.app.computer_score, 0)

    def test_computer_wins(self):
        losses = [('Rock', 'Paper'), ('Paper', 'Scissors'), ('Scissors', 'Rock')]
        for player, computer in losses:
            self.app.player_score = 0
            self.app.computer_score = 0
            result = self.app.get_result(player, computer)
            self.assertEqual(result, "Computer Wins")
            self.assertEqual(self.app.player_score, 0)
            self.assertEqual(self.app.computer_score, 1)

if __name__ == "__main__":
    unittest.main()
