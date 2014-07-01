import unittest

import game

class GameTest(unittest.TestCase):
    def test_game_can_be_created(self):
        # Arrange
        tictactoe = game.Game()

        # act
        # no actions

        # Assert
        for r in range(0, 2):
            for c in range(0, 2):
                self.assertEqual(0, tictactoe.get_cell(r, c), "Testing row {0}, col {1}".format(r, c))

    def test_cell_can_be_played(self):
        # Arrange
        tictactoe = game.Game()
        current_player = tictactoe.current_player

        # Act
        tictactoe.play_cell(1, 2)

        # Assert
        self.assertEqual(current_player, tictactoe.get_cell(1, 2))


    def test_game_can_be_won(self):
        # Arrange
        tictactoe = game.Game()
        initially_won = tictactoe.has_won

        # Act
        tictactoe.play_cell(0, 0)
        tictactoe.switch_players()
        tictactoe.play_cell(1, 0)
        tictactoe.switch_players()
        tictactoe.play_cell(1, 1)
        tictactoe.switch_players()
        tictactoe.play_cell(2, 0)
        tictactoe.switch_players()
        tictactoe.play_cell(2, 2)

        # Assert
        self.assertFalse(initially_won)
        self.assertTrue(tictactoe.has_won)

    def test_no_empty_but_non_winning_game_has_not_won(self):
        # Arrange
        tictactoe = game.Game()

        # Act
        tictactoe.play_cell(0, 0)
        tictactoe.switch_players()
        tictactoe.play_cell(1, 0)
        tictactoe.switch_players()
        tictactoe.play_cell(1, 1)
        tictactoe.switch_players()
        tictactoe.play_cell(2, 0)
        tictactoe.switch_players()
        tictactoe.play_cell(2, 1)
        tictactoe.switch_players()
        tictactoe.play_cell(2, 2)

        # Assert
        self.assertFalse(tictactoe.has_won)


    def test_cannot_play_an_already_played_cell(self):
        # Arrange
        tictactoe = game.Game()

        # act
        tictactoe.play_cell(1, 2)
        with self.assertRaises(Exception):
            tictactoe.play_cell(1, 2)


            # def test_missing(self):
            # excpect = 2
            #     real = 3
            #     self.assertEquals(excpect, real)

