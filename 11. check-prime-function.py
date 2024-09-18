
def getUserInput():
    userInput = int(input("Enter a number: "));
    return userInput;
    
def isPrime(number):
    if number > 1:
        for index in range(2, (number//2) + 1):
            if(number % index == 0):
                return False;
        return True;
    else:
        return False;

def printOutcome(primeOutcome, userInput):
    if primeOutcome:
        print(f"{userInput} is a prime number.");
    else:
        print(f"{userInput} is not a prime number.");

userInput = getUserInput();
printOutcome(isPrime(userInput), userInput);
