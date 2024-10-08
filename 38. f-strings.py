from datetime import datetime

name = input("What is your name? ");
age = int(input("What is your age? "));
year = datetime.now().year;
yearsHundred = year - age + 100;
copies = input("How many copies would you like to show?\n")

for index in range(int(copies)):
    print(f'Your name is {name} and is {age} years old. You will be {yearsHundred} from 100 years from today.');
