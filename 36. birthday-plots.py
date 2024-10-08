import json

if __name__ == "__main__":
    scientist = [];
    
    filePath = "practice-python-exercises/files/scientist-data.json";
    with open(filePath, "r") as file:
        scientist = json.load(file);
        
    print(scientist);
    # Cant get bokeh to work

