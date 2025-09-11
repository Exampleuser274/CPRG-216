x = input('first number? ')
y = input('second number? ')
z = input('third number? ')
if y > x:
    x = y
if z > x:
    x = z
print('the largest number is',x)