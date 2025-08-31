import copy
import csv
from tictactoe import tictactoe, tictactoeGeneral


def minmax(board: tictactoe, player, depth):
    #base case: the game ends
    state = board.check_winner()
    if state == 1:
        return (2, None)
    elif state == -1:
        return (-2, None)
    elif state == "draw":
        return (0, None)
    
    #if the game is undecided
    #if curr player is 1, we maximize
    if player == 1:
        #the best score is supposed to be -infinity at start
        #the goal here is to minimize the score as the opponent,
        #so we get their optimal move
        best_score = -100
        best_move = None
        #test out player1's moves
        for move in board.possible_moves():
            new = copy.deepcopy(board)
            #play the given move on a copy of the board
            new.make_move(move[0],move[1])
            #recursively call minmax to get the score for the current state
            score = minmax(new, -player, depth+1)[0]
            #if the current board state score is better than the previous, update
            if score > best_score:
                best_score = score
                best_move = move
        return (best_score, best_move)
    else: #same thing but minimizing
        best_score = 100
        best_move = None
        for move in board.possible_moves():
            new = copy.deepcopy(board)
            new.make_move(move[0],move[1])
            score = minmax(new, -player, depth+1)[0]
            # print(move, score, depth)
            if score < best_score:
                best_score = score
                best_move = move
        return (best_score, best_move)


# board = tictactoe()
# board.make_move(1,1)
# board.make_move(0,0)
# board.make_move(0,1)
# board.show_board()
# print(board.check_winner())
# print(minmax(board, -1, 0))

         
# board = tictactoe()
# board.make_move(1,1)
# board.make_move(0,0)
# board.make_move(0,1)
# board.make_move(2,1)
# board.make_move(0,2)
# board.make_move(1,0)
# board.make_move(2,0)
# board.show_board()
# print(board.check_winner())
            
# board = tictactoe()
# board.make_move(1,1)
# board.make_move(0,0)
# board.make_move(0,1)
# print(minmax(board, -1))
# board.show_board()
# print(board.check_winner())
    
# board = tictactoe()
# board.make_move(1,1)
# board.make_move(0,0)
# board.make_move(0,1)
# board.make_move(2,1)
# board.make_move(0,2)
# board.make_move(2,0)
# board.make_move(1,1)
# board.make_move(1,0)
# board.make_move(2,2)
# print(board.check_winner())

def board_to_tuple(board):
    return (tuple(board[0]),tuple(board[1]),tuple(board[2]))

step = 0

class search:
    
    def __init__(self) -> None:
        self.step = 0

    def minmaxtable(self, board: tictactoe, player, depth, table):

        self.step += 1
        print(self.step)
        state = board.check_winner()
        if state == 1:
            print("X won!")
            return (2, None)
        elif state == -1:
            print("O won!")
            return (-2, None)
        elif state == "draw":
            print("Draw!")
            return (0, None)
        
        if player == 1:
            best_score = -100
            best_move = None
            for move in board.possible_moves():
                new = copy.deepcopy(board)
                new.make_move(move[0],move[1])

                if board_to_tuple(board.board) in table:
                    return table[board_to_tuple(board.board)]
                
                score = self.minmaxtable(new, -player, depth+1, table)[0]
                if score > best_score:
                    best_score = score
                    best_move = move

            if board_to_tuple(board.board) not in table:
                table[board_to_tuple(board.board)] = (best_score,best_move, depth)

            return (best_score, best_move)
        else:
            best_score = 100
            best_move = None
            for move in board.possible_moves():
                new = copy.deepcopy(board)
                new.make_move(move[0],move[1])

                if board_to_tuple(board.board) in table:
                    return table[board_to_tuple(board.board)]

                score = self.minmaxtable(new, -player, depth+1, table)[0]
                if score < best_score:
                    best_score = score
                    best_move = move
                
            if board_to_tuple(board.board) not in table:
                table[board_to_tuple(board.board)] = (best_score, best_move, depth)

            return (best_score, best_move, depth)



def export_table_to_csv(table, filename='minmax_table.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Board State', 'Score', 'Best Move', 'Depth'])

        for board_state, (score, move, depth) in table.items():
            writer.writerow([str(board_state), score, move, depth])



def play():
    board = tictactoeGeneral(4)
    humangoesfirst = False
    table = {}
    engine = search()


    if humangoesfirst:
        print("human goes first")
        turn = 1
        while board.check_winner() == None:
            print("\n")
            board.show_board()
            print("\n")
            if turn == 1:
                move = input("enter a move in the format row,col: ")
                move = move.strip().split(",")
                board.make_move(int(move[0]), int(move[1]))
            else:
                data = engine.minmaxtable(board, turn, 0, table)
                move = data[1]
                # move = minmax(board, 1, 0)
                board.make_move(move[0], move[1])
                print("evaluation: {}".format(data[0]))
            
            turn *= -1
        board.show_board()
    else:
        print("bot goes first")
        turn = 1
        while board.check_winner() == None:
            print("\n")
            board.show_board()
            print("\n")
            if turn != 1:
                move = input("enter a move in the format row,col: ")
                move = move.strip().split(",")
                board.make_move(int(move[0]), int(move[1]))
            else:
                data = engine.minmaxtable(board, turn, 0, table)
                move = data[1]
                # move = minmax(board, 1, 0)
                board.make_move(move[0], move[1])
                print("evaluation: {}".format(data[0]))
            
            turn *= -1
        board.show_board()

# play()

engine = search()
board = tictactoeGeneral(4)
table = {}
engine.minmaxtable(board, 1, 0, table)
export_table_to_csv(table, "tictactoe4x4Table.csv")


#this used to cause a bug where the engine didn't detect the threat at 1,0
# it turned out to be because the engine didn't think it was 1's turn

# board = tictactoe()
# board.make_move(1,1)
# board.make_move(0,0)
# board.make_move(1,1)
# board.make_move(2,2)
# board.make_move(2,0)
# board.show_board()
# print(minmax(board, 1, 0))