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

# TODO
def displayGuess(word, lettersGuessed):
    wordToDisplay = "";
    
    for letter in word.lower():
        if letter in lettersGuessed:
            wordToDisplay += letter;
            wordToDisplay += "_ ";
        else:
            wordToDisplay += "_ ";
    
    print(wordToDisplay);

def startGame():
    filePath = "practice-python-exercises/files/SOWPODS-dictionary.txt";
    wordToGuess = "EVAPORATE";
    lettersGuessed = set();
    wordSet = set(wordToGuess.lower());
    
    words = readFromFile(filePath);
    # wordToGuess = pickRandomWord(words);
    
    print(wordToGuess);
    
    print("Welcome to Hangman!");
    print("-------------------");
    print("_ " * len(wordToGuess));

    # Test cases for player input
    # A, AA, " ", . , 1, !, 1A, "enter", "exit" 
    # playerGuess = "a";
    # playerGuess = "aa";
    # playerGuess = "AA";
    # playerGuess = " ";
    # playerGuess = ".";
    # playerGuess = "1";
    # playerGuess = "!";
    # playerGuess = "1A";
    # playerGuess = "A1";
    # playerGuess = "enter";
    # playerGuess = "exit";
    
    # Test cases if in letter
    # playerGuess = "a";
    # playerGuess = "z";
    # print(validGuess(playerGuess));
    
    while not wordSet.issubset(lettersGuessed):
        playerGuess = input("\nGuess your letter: ");
        if validGuess(playerGuess):
            if playerGuess not in lettersGuessed:
                if letterIsInWord(wordToGuess, playerGuess):
                    lettersGuessed.add(playerGuess.lower().strip());
                    displayGuess(wordToGuess, lettersGuessed);
                else:
                    print(f"Incorrect! {playerGuess} is not in word.");
            else:
                print(f"You have already guessed {playerGuess}.");
                
    print(f"The word is {wordToGuess}.");
            
            
    # user inputs letter
    # checks if letter is valid
        # valid -> check is letter has been guessed
            # check if letter is in word
                # add letter to guessed letters
                # display letters in word
                    # allow user to guess again
            
        # not valid -> display error
            # user is guess letter again
        
    

startGame();