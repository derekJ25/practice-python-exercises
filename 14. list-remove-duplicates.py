
def removeDupeSet(names):
    return set(names);

def removeDupeList(names):
    newNames = [];
    # loop through names
    for name in names:
        if name not in newNames:
            newNames.append(name);
    return newNames;
        
        
            

names = ["Michele", "Robin", "Sara", "Michele"]

print(names);
print(removeDupeSet(names));
print(removeDupeList(names));