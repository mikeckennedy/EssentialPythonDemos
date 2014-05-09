import unittest

import app


class GameTests(unittest.TestCase):
    def test_can_be_created(self):
        # Arrange
        game = app.Game()

        # Act (empty)

        # Assert
        b = game.board
        self.assertEqual(3, len(b))
        for row in b:
            self.assertEqual(3, len(row))

    def test_game_can_track_and_switch_players(self):
        # Arrange
        game = app.Game()
        first_player = game.current_player
        print("First player is " + str(first_player))

        # Act
        game.swap_players()

        # Assert
        self.assertNotEqual(first_player, game.current_player)

    def test_game_can_be_won(self):
        # Arrange
        game = app.Game()

        #act
        game.play_cell(0, 0)
        game.swap_players()
        game.play_cell(1, 2)
        game.swap_players()
        game.play_cell(1, 1)
        game.swap_players()
        game.play_cell(2, 1)
        game.swap_players()
        game.play_cell(2, 2)

        #assert
        self.assertTrue(game.has_winner)

    def test_is_error_to_play_played_cell(self):
        game = app.Game()

        game.play_cell(1, 1)
        game.swap_players()
        with self.assertRaises(Exception):
            game.play_cell(1, 1)

            # only pass if this crashes...












