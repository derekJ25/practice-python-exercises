import random
import sys

randNum = random.randint(1, 9);
guessCount = 0;
userInput = 0;

while userInput != randNum and userInput != "exit":
    userInput = input("Guess the random number (1-9) or 'exit' to quit: ");
    if userInput == "exit":
        sys.exit();
    
    if int(userInput) > randNum:
        print("Guess is too high.");
    elif int(userInput) < randNum:
        print("Guess is too low.");
    else: 
        print(f"Congratulations! The number was {randNum}.");
        print(f"You guessed it in {guessCount} tries.");
        sys.exit();
    guessCount += 1;
