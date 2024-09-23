import random

def generateRandomList():
    MIN = 0;
    MAX = 10;
    AMOUNT = 10;
    count = 0;
    randList = [];
    while count < AMOUNT:
        randList.append(random.randint(MIN, MAX));
        count += 1;
    randList.sort();
    return randList;

# # Regular search
# def isNumInList(list, num):
#     return True if num in list else False;

# Binary search
def isNumInList(list, num):
    low = 0;
    high = len(list) - 1;
    middle = 0;
    
    while (low <= high):
        middle = (low + high) / 2;
        if list[middle] < num:
            low = middle + 1;
        elif list[middle] > num:
            high = middle - 1;
        else:
            return middle;
    return -1;
        
    

if __name__=="__main__":
    list = generateRandomList();
    print(list);
    isNumInList(list, 0);
    # userInput = int(input("Enter a number: "));
    # print(f'{userInput} is in {list}.') if isNumInList(list, userInput) else print(f'{userInput} is not in {list}.');