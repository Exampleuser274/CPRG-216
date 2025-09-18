#Third class demo
'''
In this class we will work on variables, operators and other stuff
'''

#Review
#assignment
w = "four" #string
x = 4 #integer
y = 4.0 #float
z = False #bool
print("The variable w is",w,"and the type is",type(w))
print("the variable x is",x,"and the type is",type(x))
print("the variable y is",y,"and the type is",type(y))
print("the variable z is",z,"and the type is",type(z))

#some functions call: print, input, int, float, str, bool

strnum = "43"
intnum = int(strnum) #convert to int
num = 3
num_f = float(num)
num2 = 3.4
num2_i = int(num2)
num2str = str(num2)
#printing the string and int
print(intnum)
print(strnum)

#using input

yob = input("enter year of birth\n")
age = 2025 - int(yob)
print("your age is",age)


#Program
user_input = input("What is the radius?\n")
r = int(user_input)
PI = 22/7
area = PI * r**2
circ = 2*PI*r
print("the circumference is", circ, 'and the area is', area)

user_input = input("what is the side length of the square?\n")
side = int(user_input)
area = side**2
print("the area is",area)