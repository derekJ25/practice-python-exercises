
fileName = "practice-python-exercises/files/sampleFile.txt";

# with open(fileName, "w") as open_file:
#     open_file.write("Created a new file\n");
#     open_file.write("Hello this is a sample file\n");
#     open_file.write("Bye bye");

open_file = open(fileName, 'w')
open_file.write("Created a new file\n");
open_file.write("Hello this is a sample file\n");
open_file.write("Bye bye.");
open_file.close()