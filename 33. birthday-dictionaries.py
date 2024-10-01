

if __name__ == "__main__":
    birthdays = {
            "Jack": "13/2/1995",
            "Fred": "15/7/1990",
            "Jeff": "2/10/1998" 
    }
    
    print("Welcome to the birthday dictionary. We know the bithday of: ");
    for person in birthdays:
        print(person);
    input = input("Who's birthday do you want to look up?\n");
    if input in birthdays:
        print("{}\'s birthday is {}".format(input, birthdays[input]));
    else:
        print(f"{input} birthday does not exist in the system.")
        
        