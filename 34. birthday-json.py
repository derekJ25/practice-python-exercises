import json
import sys

def addData():
    name = input("Enter name to add to JSON: ");
    dateOfBirth = input("Enter date of birth: ");
    # birthdays[name] = dateOfBirth;
    birthdays.update({name: dateOfBirth});
    
    with open(filePath, "w") as file:
        json.dump(birthdays, file);
    
    print("{} has been added to file.\n".format(name))
        
def displayData():
    print("Birthdays:");
    for key in birthdays:
        print(key.ljust(8), ": ", birthdays[key]);
    print();
        
def findData():
    name = input("Who would you like to find? ").strip();
    try:
        if birthdays[name]:
            print("{} is born on {}.\n".format(name, birthdays[name]));
    except KeyError:
        print("{} is not in file.\n".format(name));

if __name__ == "__main__":
    filePath = "practice-python-exercises/files/info.json";
    birthdays = {};
    
    with open(filePath, "r") as file:
        birthdays = json.load(file);
    
    displayData();
    
    while True:
        choice = input("What do you want to do? Add/Find/Display/Exit: ");
        print();
        if choice == "add":
            addData();
        elif choice == "find":
            findData();
        elif choice == "display":
            displayData();
        elif choice == "exit":
            sys.exit();
        else:
            print(f"{choice} is not a valid choice. Please try again.");
    
    
    
    
    