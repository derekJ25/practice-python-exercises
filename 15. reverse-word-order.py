
def reverseWord(string):
    # stringList = string.split(" ");
    # reverseString = " ".join(stringList[::-1]);
    # return reverseString;
    
    # or can have one liner
    return " ".join(string.split(" ")[::-1])

string =  "My name is Michele";
print(reverseWord(string));