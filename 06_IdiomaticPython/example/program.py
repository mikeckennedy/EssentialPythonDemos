from game import Game


class Program(object):
    def __init__(self):
        self.game = Game()

    def run(self, max_times):
        game = self.game
        board = game.board

        # Print out cheesy welcome
        self.Print_welcome_message()

        print("The board is set:")
        print(board)

        while not game.has_winner:
            # print who's turn it is (X or O)
            print("It's {0}'s turn!".format(game.current_player_name))

            # get the value of the player who's turn it currently is.
            row, col = self.query_placement_from_user()

            # verify that entry is not already chosen
            if game.cell_already_played(row, col):
                print("Sorry, that position is already occupied with a {0}!"
                      .format(game.get_cell(row, col)))
                print("try again")
                print(board)
                print()
                continue

            # play the cell
            game.play_cell(row, col)

            print("Excellent choice:")
            print(board)

            print()

            # check for a winner
            print("We're checking for a winner...")
            if not game.has_winner:
                print("No winner yet, keep going!")
                print()

            game.switch_players()

            # there may be a bug here. :) delete the line if you think so AFTER
            # pylint tells you so.
            print("Continue player {0}".format(name_of_app_runner))

        # Announce winner and show the winning board.
        print("We have a winner! It's the " + game.find_winner() + "'s!")
        print("Way to win the day")
        print()
        print(board)


    def Print_welcome_message(self):
        print("Welcome to tic-tac-toe profession v0.1")
        print()


    def print_current_player(self):
        if self.game.active_player == self.game.x:
            print("It's X's turn.")
        else:
            print("It's O's turn.")




    def query_placement_from_user(self):
        row = int(input("Choose row (zero based): "))
        col = int(input("Choose column (zero based): "))
        return row, col