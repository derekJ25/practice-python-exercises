EMPTY_CELL = " ";

def startGame():
    board = [[EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
         [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
         [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]];
    playerOneTurn = True;
    turnCount = 0;
    
    print("Welcome to tic-tac-toe!");
    print("Coordinates are row, col where row & col are between 0 & 2 (inclusive).");
    while not checkBoard(board) and turnCount < 9:
        displayBoard(board);
        printPlayerTurn(playerOneTurn);
        playerInput = input("P1 - Please enter coordinates row,col: ") if playerOneTurn else input("P2 - Please enter coordinates row,col: ");
        while not validInput(playerInput):
            playerInput = input("P1 - Please enter coordinates row,col: ") if playerOneTurn else input("P2 - Please enter coordinates row,col: ");
        if checkCell(board, playerInput):
            coordinate = playerInput.split(",");
            board[int(coordinate[0])][int(coordinate[1])] = "x" if playerOneTurn else "o";
            playerOneTurn = not playerOneTurn;
            turnCount += 1;
            print(turnCount);

    
def printPlayerTurn(playerOneTurn):
    print("Player 1 turn. You are x's.") if playerOneTurn else print("Player 2 turn. You are o's.");
    
def validInput(playerInput):
    input = playerInput.split(",");
    
    if len(input) != 2:
        print("Please enter a valid input. row,col where row and col are between 0 and 2 (inclusive).");
        return 0;
    else:
        try:
            if (0 <= int(input[0]) <= 2) and (0 <= int(input[1]) <= 2):
                return 1;
            return 0;
        except ValueError:
            print("Please enter numbers only. row,col where row and col are between 0 and 2 (inclusive).");
            return 0;

def checkCell(board, userInput):
    coordinate = userInput.split(",");
    row = int(coordinate[0]);
    col = int(coordinate[1]);
    if board[row][col] == EMPTY_CELL:
        return 1;
    else:
        print("Cell is already filled. Please try again.");
        return 0;

def checkBoard(board): 
    # check row
    for index in range(0, 3):
        row = set([board[index][0], board[index][1], board[index][2]]);
        if len(row) == 1 and board[index][0] != 0:
            if board[index][0] == "x":
                print("Player 1 wins!");
            elif board[index][0] == "o":
                print("Player 2 wins!");
            else:
                return 0;
            return 1;
    
    # check column
    for index in range(0, 3):
        col = set([board[0][index], board[1][index], board[2][index]]);
        if len(col) == 1 and board[0][index] != 0:
            if board[0][index] == "x":
                print("Player 1 wins!");
            elif board[0][index] == "o":
                print("Player 2 wins!");
            else:
                return 0;
            return 1;
    
    # check diagonal
    for index in range(0, 3):
        diagonalOne = set([board[0][0], board[1][1], board[2][2]]);
        diagonalTwo = set([board[index][2], board[index][1], board[index][0]]);
        if len(diagonalOne) == 1 or len(diagonalTwo) == 1 and board[1][1] != 0:
            if board[1][1] == "x":
                print("Player 1 wins!");
            elif board[1][1] == "o":
                print("Player 2 wins!");
            else:
                return 0;
            return 1;
    
    # check gameboard
    for index in board:
        if 0 in index:
            return 0;
    
    return 1;

def displayBoard(board):
    print(f' ---' * 3);
    print(f'| {board[0][0]} | {board[0][1]} | {board[0][2]} |');
    print(f' ---' * 3);
    print(f'| {board[1][0]} | {board[1][1]} | {board[1][2]} |');
    print(f' ---' * 3);
    print(f'| {board[2][0]} | {board[2][1]} | {board[2][2]} |');
    print(f' ---' * 3);

startGame();
