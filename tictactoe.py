

class tictactoeGeneral:
    def __init__(self, size=3) -> None:
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.winner = None
        self.turn = 1
        self.size = size

    
    def make_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.turn
            if self.turn == 1:
                self.turn = -1
            else:
                self.turn = 1
        else:
            pass
    
    def possible_moves(self):
        final = []

        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    final.append((row, col))
        return final

    def check_winner(self):
        for row in range(self.size):
            temp = 0
            for col in range(self.size):
                temp += self.board[row][col]
            if temp == self.size or temp == -self.size:
                return temp//self.size
            
        for col in range(self.size):
            temp = 0
            for row in range(self.size):
                temp += self.board[row][col]
                
            if temp == self.size or temp == -self.size:
                return temp//self.size

        temp = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if temp == self.size or temp == -self.size:
                return temp//self.size
        temp = self.board[2][0] + self.board[1][1] + self.board[0][2]
        if temp == self.size or temp == -self.size:
                return temp//self.size

        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    return None
        return "draw"
    
    def show_board(self):
        for row in self.board:
            print(row)

class tictactoe(tictactoeGeneral):
    def __init__(self) -> None:
        super().__init__(3)


game = tictactoeGeneral(4)
game.show_board()
print(game.possible_moves())
