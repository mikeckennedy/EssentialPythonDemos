from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.x = self.board.x
        self.o = self.board.o
        self.active_player = self.x

    @property
    def has_winner(self):
        return not self.find_winner() is None

    @property
    def current_player_name(self):
        return "X" if self.active_player == self.x else "O"

    @property
    def winner(self):
        if not self.has_winner:
            return "No winner"

        return "X" if self.find_winner() == self.x else "O"

    def find_winner(self):
        board = self.board
        winner = None
        for i in range(3):
            sums = [
                board.cells[0][0] + board.cells[0][1] + board.cells[0][2],  # row 1
                board.cells[1][0] + board.cells[1][1] + board.cells[1][2],  # row 2
                board.cells[2][0] + board.cells[2][1] + board.cells[2][2],  # row 3
                board.cells[0][0] + board.cells[1][0] + board.cells[2][0],  # col 1
                board.cells[0][1] + board.cells[1][1] + board.cells[2][1],  # col 2
                board.cells[0][2] + board.cells[1][2] + board.cells[2][2],  # col 3
                board.cells[0][0] + board.cells[1][1] + board.cells[2][2],  # diagonal 1
                board.cells[0][2] + board.cells[1][1] + board.cells[2][0]  # diagonal 2
            ]

            if 3 in sums:
                winner = "X"

            if -3 in sums:
                winner = "O"

        return winner


    def cell_already_played(self, row, col):
        return not self.board.cells[row][col] == self.board.empty

    def get_cell(self, row, col):
        return self.board.cells[row][col]

    def play_cell(self, row, col):
        self.board.cells[row][col] = self.active_player

    def switch_players(self):
        self.active_player = self.x if self.active_player == self.o else self.o

