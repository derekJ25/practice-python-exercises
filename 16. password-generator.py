import random
import string

def generatePassword(length):
    password = "";
    index = 0;
    while index < length:
        rand = random.randint(1, 4);
        if rand == 1:
            password += generateLowercase();
        elif rand == 2:
            password += generateUppercase();
        elif rand == 3:
            password += str(generateNumber());
        else:
            password += generateSymbol();
        index += 1;
    
    return password;

def generateLowercase():
    letters =  string.ascii_lowercase;
    return letters[random.randint(0, len(letters) - 1)];

def generateUppercase():
    letters =  string.ascii_uppercase;
    return letters[random.randint(0, len(letters) - 1)];

def generateNumber():
    numbers = string.digits;
    return numbers[random.randint(0, len(numbers) - 1)];

def generateSymbol():
    symbols = string.punctuation;
    return symbols[random.randint(0, len(symbols) - 1)];


lengthOfPassword = int(input("How long would you like your password to be: "));
while lengthOfPassword <= 0:
    lengthOfPassword = int(input("How long would you like your password to be: "));

print(generatePassword(lengthOfPassword));

