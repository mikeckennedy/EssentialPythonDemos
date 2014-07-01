class Game:
    def __init__(self):
        self.empty = 0
        self.x = 1
        self.current_player = self.x
        self.o = -1
        self.board = self.get_empty_board()

    def get_cell(self, row, col):
        return self.board[row][col]

    def get_empty_board(self):
        e = self.empty
        return [
            [e, e, e],
            [e, e, e],
            [e, e, e]
        ]

    def not_run(self):
        x = 2
        y = 3
        z = 4

    def play_cell(self, r, c):
        cell = self.board[r][c]
        if cell != self.empty:
            raise Exception("Cannot play already played cell")

        self.board[r][c] = self.current_player

    def switch_players(self):
        self.current_player *= -1

    @property
    def has_won(self):
        b = self.board
        possible_wins = [
            [b[0][0], b[0][1], b[0][2]],  # first row
            [b[1][0], b[1][1], b[1][2]],  # Second row
            [b[2][0], b[2][1], b[2][2]],  # third row
            [b[0][0], b[1][0], b[2][0]],  # first column
            [b[0][1], b[1][1], b[2][1]],  # second column
            [b[0][2], b[1][2], b[2][2]],  # third column
            [b[0][0], b[1][1], b[2][2]],  # diag 1
            [b[0][2], b[1][1], b[2][0]],  # daig 2
        ]

        wins = [
            sum(w)/3
            for w in possible_wins
            if sum(w) == -3 or sum(w) == 3
        ]

        if wins:
            print(wins)
            return True

        return False
