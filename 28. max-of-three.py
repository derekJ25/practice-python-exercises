import random

def max(values):
    max = 0;
    for num in values:
        if num > max:
            max = num;
    return max;

def generateValues():
    values = [];
    LENGTH = 10;
    MIN = 0;
    MAX = 100;
    for i in range(LENGTH):
        values.append(random.randint(MIN, MAX));
    return values;

values = generateValues();
print(values);
print(max(values));