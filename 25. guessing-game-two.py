
def cpuGuessNumber(MIN, MAX):
    middle = int((MIN + MAX) / 2);
    return middle;   

def startGuessingGame():
    MIN = 0;
    MAX = 100;
    cpuGuessCount = 1;
    cpuGuess = 0;
    
    userNum = int(input("Enter number for CPU to guess (0 - 100): "));
    while cpuGuess != userNum:
        cpuGuess = cpuGuessNumber(MIN, MAX);
        print(f'CPU guess {cpuGuess}.');
        
        userNum = input("Enter too high/too low/correct: ");
        if userNum == "too high":
            MAX = cpuGuess - 1;
            cpuGuessCount += 1;
        elif userNum == "too low":
            MIN = cpuGuess + 1;
            cpuGuessCount += 1;
        elif userNum == "correct":
            print(f'CPU guessed in {cpuGuessCount} tries.');
            break;
        else: 
            print("Please enter a valid input.");
            userNum = input("Enter too high/too low/correct: ");
    
startGuessingGame();
