
def checkBoard(board):
    
    # check row
    for index in range(0, 3):
        row = set([board[index][0], board[index][1], board[index][2]]);
        if len(row) == 1 and board[index][0] != 0:
            return board[index][0];
    
    # check column
    for index in range(0, 3):
        col = set([board[0][index], board[1][index], board[2][index]]);
        if len(col) == 1 and board[0][index] != 0:
            return board[0][index];
    
    # check diagonal
    for index in range(0, 3):
        diagonalOne = set([board[0][0], board[1][1], board[2][2]]);
        diagonalTwo = set([board[index][2], board[index][1], board[index][0]]);
        if len(diagonalOne) == 1 or len(diagonalTwo) == 1 and board[1][1] != 0:
            return board[1][1];
    
    return 0;

# game = [[0, 0, 0], 
#         [0, 0, 0], 
#         [0, 0, 0]];

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

winner_row_2 = [[2, 2, 2],
                [0, 1, 1],
                [1, 0, 2]];

print(checkBoard(winner_is_2));
print(checkBoard(winner_is_1));
print(checkBoard(winner_is_also_1));
print(checkBoard(no_winner));
print(checkBoard(also_no_winner));
print(checkBoard(winner_row_2));
