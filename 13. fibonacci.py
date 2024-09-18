
def fibonacci(num):
    index = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while index < (num - 1):
            fib.append(fib[index] + fib[index - 1])
            index += 1
    return fib;

userInput = int(input("Enter number: "));
print(fibonacci(userInput));
