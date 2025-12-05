from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")

    def start(self):
        current = self.player1

        while True:
            self.board.print_board()
            print(f"{current.name} ({current.symbol}) — Enter row and column: ")

            try:
                row = int(input("Row: "))
                col = int(input("Col: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid coordinates! Try again.")
                continue

            if not self.board.play_move(row, col, current.symbol):
                print("Cell already occupied! Try again.")
                continue

            if self.board.check_win(current.symbol):
                self.board.print_board()
                print(f"{current.name} wins!")
                break

            if self.board.is_full():
                self.board.print_board()
                print("Draw!")
                break

            current = self.player2 if current == self.player1 else self.player1
x=1
x=2

if __name__ == "__main__":
    Game().start()
