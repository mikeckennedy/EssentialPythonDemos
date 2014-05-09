class Game:
    def __init__(self):
        self.empty = 0
        self.x = 1
        self.o = -1
        self.current_player = self.x
        self.board = self.build_empty_board()

    def build_empty_board(self):
        e = self.empty
        return [
            [e, e, e],
            [e, e, e],
            [e, e, e]
        ]

    def swap_players(self):
        self.current_player *= -1

    def play_cell(self, row, col):
        if self.board[row][col] != self.empty:
            raise Exception("Cannot play played cell!")
        self.board[row][col] = self.current_player

    @property
    def has_winner(self):
        return self.find_winner()

    def other(self):
        print("Hi!")

    def find_winner(self):
        b = self.board
        wins = [
            [b[0][0], b[1][1], b[2][2]],
            [b[2][0], b[1][1], b[0][2]],
            [b[0][0], b[0][1], b[0][2]]
        ]

        for w in wins:
            s = sum(w)
            if s == -3:
                return self.y
            if s == 3:
                return self.x

        return None