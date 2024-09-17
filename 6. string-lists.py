string = input("Enter a string: ");

def isPalindrome(string):
    return True if string[::-1] == string else False;
    
print(isPalindrome(string));