
def printHorizontalLine():
    print(" ---" * boardSize);
    
def printVerticalLine():
    print("|   " * (boardSize + 1)) ;

def printGameboard(boardSize):
    for index in range(boardSize):
        printHorizontalLine();
        printVerticalLine();
    printHorizontalLine();
    
boardSize = int(input("Enter size of board: "));
printGameboard(boardSize);
    