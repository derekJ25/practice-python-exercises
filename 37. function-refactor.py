
def printVertical(amount):
    verticalStr = "|";
    for index in range(amount):
        verticalStr += "   |";
    print(verticalStr);

def printHorizontal(amount):
    horizontalStr = "";
    for index in range(amount):
        horizontalStr += " ---";
    print(horizontalStr);

def printBoard(amount):
    printHorizontal(amount);
    for index in range(amount):
        printVertical(amount);
        printHorizontal(amount);

if __name__ == "__main__":
    AMOUNT = 4;
    
    printBoard(AMOUNT);