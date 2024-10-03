import json
from collections import Counter

if __name__ == "__main__":
    filePath = "practice-python-exercises/files/info.json";
    with open(filePath, "r") as file:
        birthdays = json.load(file);
        
    monthToString = {
        1: "January",
        2: "February",
        3: "March", 
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    
    months = [];
    for name in birthdays.items():
        month = int(name[1].split("/")[1]);
        months.append(monthToString[month]);
    
    print(Counter(months));