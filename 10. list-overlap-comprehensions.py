import random;

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = random.sample(range(1,20), 12);
b = random.sample(range(1,20), 16);
 
list = [num for num in a if num in b];
print(list);
 