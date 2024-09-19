import random
import sys

def generateRandomNumber():
    lengthOfNumber = 4;
    count = 0;
    randNum = "";
    while(count < lengthOfNumber):
        randNum += str(generateRandomDigit());
        count += 1;
    return randNum;

def generateRandomDigit():
    MIN = 0;
    MAX = 9;
    return random.randint(MIN, MAX);

def displayCowBull(numToGuess, guess):
    cows = 0;
    bulls = 0;
    guessStr = str(guess);
    
    if len(guessStr) <= len(numToGuess):
        for index in range(len(guessStr)):
            if numToGuess[index] == guessStr[index]:
                cows += 1;
            else:
                bulls += 1;
    print(f'{cows} cows, {bulls} bulls');
    
if __name__=="__main__":
    print("Welcome to the Cows and Bulls Game!");
    guessCount = 0;
    guess = input("Enter a number or 'exit' to quit: ");
    numToGuess = generateRandomNumber();
    while(guess != numToGuess or guess == "exit"):
        guessCount += 1;
        if guess == "exit":
            sys.exit();
        displayCowBull(numToGuess, guess);
        guess = input("Enter a number or 'exit' to quit: ");
    
    print(f'Congratulations! The number was {numToGuess}. You took {guessCount} guesses.');