import random

def pickRandomWord():
    filePath = "practice-python-exercises/files/SOWPODS-dictionary.txt";
    words = [];
    with open(filePath, "r") as file:
        line = file.readline().strip();
        while line:
            words.append(line);
            line = file.readline().strip();
    
    return words[random.randint(0, len(words) - 1)];

print(pickRandomWord());