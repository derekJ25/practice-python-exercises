fileName = "practice-python-exercises/files/sampleFile.txt";
nameList = "practice-python-exercises/files/nameList.txt";

# with open(fileName, "r") as open_file:
#     line = open_file.readline();
#     while line:
#         print(line);
#         line = open_file.readline();

names = {};

with open(nameList, "r") as open_file:
    line = open_file.readline();
    while line:
        line = line.strip();
        if line in names:
            names[line] += 1;
        else:
            names[line] = 1;
        line = open_file.readline();
        
print(names);
