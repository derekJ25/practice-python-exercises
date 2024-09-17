import sys

# # No loop
# player1 = input("Player 1 play: rock, paper or scissors? ");
# player2 = input("Player 2 play: rock, paper or scissors? ");


# if player1 == "rock":
#     if player2 == "rock":
#         print("draw");
#     elif player2 == "paper":
#         print("player 2 wins");
#     else:
#         print("player 1 wins");
# elif player1 == "paper":
#     if player2 == "rock":
#         print("player 1 wins"); 
#     elif player2 == "paper":
#         print("draw");
#     else:
#         print("player 2 wins");
# else:
#     if player2 == "rock":
#         print("player 2 wins"); 
#     elif player2 == "paper":
#         print("player 1 wins");
#     else:
#         print("draw");
            
# With loop
gameCount = 1;
exit = False;
options = ["rock", "paper", "scissors"];

def checkWinner(player1, player2):
    if player1 == "rock":
        if player2 == "rock":
            print("draw");
        elif player2 == "paper":
            print("player 2 wins");
        else:
            print("player 1 wins");
    elif player1 == "paper":
        if player2 == "rock":
            print("player 1 wins"); 
        elif player2 == "paper":
            print("draw");
        else:
            print("player 2 wins");
    else:
        if player2 == "rock":
            print("player 2 wins"); 
        elif player2 == "paper":
            print("player 1 wins");
        else:
            print("draw");

while not exit:
    print(f'Game {gameCount}!');
    validInput = False;
    while not validInput:
        player1Input = input("Player 1 play: rock, paper or scissors: ");
        player2Input = input("Player 2 play: rock, paper or scissors: ");
        if player1Input in options and player2Input in options:
            validInput = True;
        else:
            print("Invalid play options. Please try again.");
            
    checkWinner(player1Input, player2Input);
    playAnotherGame = False;
    userInput = input("Type 'yes' to play another game or 'exit' to quit: ");
    while not playAnotherGame:
        if userInput == "yes":
            gameCount += 1;
            playAnotherGame = True;
        elif userInput == "exit":
            sys.exit();
        else:
            userInput = input("Would you like to player another game? or type 'exit' to quit");
    
        
    