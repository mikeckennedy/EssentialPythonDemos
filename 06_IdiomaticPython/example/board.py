"""
   This module creates and defines the board.
"""


class Board:
    """
        This is the board that represents a game of tic-tac-toe.
        Hope you like it!
    """

    def __init__(self):
        """
        Class constructor
        """
        self.x_value = 1
        self.o_value = -1
        self.empty = 0
        self.cells = self.build_empty_board()

    def build_empty_board(self):
        """
        Creates a starting, empty board.
        :New board:
        """
        cells = [
            [self.empty, self.empty, self.empty],
            [self.empty, self.empty, self.empty],
            [self.empty, self.empty, self.empty],
        ]
        return cells

    def print_board(self):
        """
        Prints the board to the console.
        """
        for row in self.cells:
            for column in row:
                print('x'
                      if column == self.x_value
                      else ('o' if column == self.o_value else '.'),
                      end=' ')
            print()

    def __str__(self):
        text = ""
        for row in self.cells:
            for column in row:
                text += 'x' if column == self.x_value \
                    else ('o' if column == self.o_value else '.')
            text += "\n"
        return text

