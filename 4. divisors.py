x = range(2, 11);
num = int(input("Enter a number: "));

divisor = [];

for val in x:
  if val % num == 0:
    divisor.append(val);
    
print(divisor);
    
print([val for val in x if val % num == 0]);
    