primeNumberFile = "practice-python-exercises/files/primeNumberList.txt";
happyNumberFile = "practice-python-exercises/files/happyNumberList.txt";

# # method 1: read file and put into list then get find dupes and put in new list
# primeNumbers = [];
# with open(primeNumberFile, "r") as open_file: 
#     line = open_file.readline().strip();
#     while line:
#         primeNumbers.append(line);
#         line = open_file.readline().strip();

# happyNumbers = [];
# with open(happyNumberFile, "r") as open_file: 
#     line = open_file.readline().strip();
#     while line:
#         happyNumbers.append(line);
#         line = open_file.readline().strip();

# dupes = [];
# for num in primeNumbers:
#     if num in happyNumbers:
#         dupes.append(num);
        
# print(dupes);

# method 2: 
def fileToIntList(fileName):
    returnList = [];
    with open(fileName) as file:
        line = file.readline();
        while line:
            returnList.append(int(line));
            line = file.readline();
    return returnList;

primeList = fileToIntList(primeNumberFile);
happyList = fileToIntList(happyNumberFile);

dupe = [num for num in primeList if num in happyList];
print(dupe);