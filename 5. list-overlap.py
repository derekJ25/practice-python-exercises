a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

setA = set(a);
setB = set(b);

dupe = [];

maxLenSet = setA if a > b else setB;
minLenSet = setA if maxLenSet == setB else setB;

for i in maxLenSet:
    for j in minLenSet:
        if i == j:
            dupe.append(i);
            
print(dupe);

