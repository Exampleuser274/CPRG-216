import math
a = int(input("what is a?"))
b = int(input("what is b?"))
c = int(input("what is c?"))
x1 = 0
x2 = 0
error = False
if a == 0:
    x1 = x2 = -c/b
elif 4*a*c < b**2:
    x1 = (-b + (math.sqrt(b**2-4*a*c)/(2*a)))
    x2 = (-b - (math.sqrt(b**2-4*a*c)/(2*a)))
else:

    error = True
    exit
if error == False:
    print("x1 is", x1,"and x2 is", x2)
else:
    print("no solution")