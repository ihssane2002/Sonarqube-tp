class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def print_board(self):
        print("\n  0 1 2")
        for i, row in enumerate(self.grid):
            print(i, " ".join(row))

    def play_move(self, row, col, symbol):
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_win(self, symbol):
        # Check rows and columns
        for i in range(3):
            if all(self.grid[i][j] == symbol for j in range(3)):
                return True
            if all(self.grid[j][i] == symbol for j in range(3)):
                return True

        # Check diagonals
        if (self.grid[0][0] == symbol and
            self.grid[1][1] == symbol and
            self.grid[2][2] == symbol):
            return True

        if (self.grid[0][2] == symbol and
            self.grid[1][1] == symbol and
            self.grid[2][0] == symbol):
            return True

        return False

    def is_full(self):
        return all(self.grid[i][j] != " " for i in range(3) for j in range(3))
