import random
import string

def pickRandomWord(words):
    return words[random.randint(0, len(words) - 1)];

def validGuess(playerInput):
    if(len(playerInput.lower().strip()) != 1):
        return False;
    letters = list(string.ascii_lowercase);
    if playerInput not in letters:
        return False;
    return True;

def readFromFile(filePath):
    words = [];
    with open(filePath, "r") as file:
        line = file.readline().strip();
        while line:
            words.append(line);
            line = file.readline().strip();
        
    return words;

def letterIsInWord(word, guess):
    for letter in word.lower():
        if letter in guess.lower():
            return True;
    return False;

def displayGuess(word, lettersGuessed):
    wordToDisplay = "";
    
    for letter in word.lower():
        if letter in lettersGuessed:
            wordToDisplay += letter;
            wordToDisplay += " ";
        else:
            wordToDisplay += "_ ";
    
    print(wordToDisplay);

if __name__ == '__main__':
    filePath = "practice-python-exercises/files/SOWPODS-dictionary.txt";
    words = readFromFile(filePath);
    wordToGuess = pickRandomWord(words);
    lettersGuessed = set();
    wordSet = set(wordToGuess.lower());
    guessCount = 6;
    
    print("Welcome to Hangman!");
    print("-------------------");
    print("_ " * len(wordToGuess));
    
    while not wordSet.issubset(lettersGuessed) and guessCount > 0:
        playerGuess = input("\nGuess your letter: ").lower();
        if validGuess(playerGuess):
            if playerGuess not in lettersGuessed:
                if letterIsInWord(wordToGuess, playerGuess):
                    lettersGuessed.add(playerGuess.lower().strip());
                    displayGuess(wordToGuess, lettersGuessed);
                else:
                    print(f"Incorrect! {playerGuess} is not in word.");
                    guessCount -= 1;
                print(f"You have {guessCount} guesses left.");
            else:
                print(f"You have already guessed {playerGuess}.");
    
    if guessCount == 0:
        print("\nGAME OVER!\n");
                
    print(f"The word is {wordToGuess}.");
            
        