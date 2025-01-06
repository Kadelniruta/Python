#What is function?
# function in Python is a block of reusable and organized code that is used to perform a specific task

# types of function
# 1. Built-in function : print(), input( ), type() etc are examples of built-in functions
# 2. User defined function: A function which is created by the user using the keyword

# Arguments/ parameter
# function with parameter
# def hello(name):
#     print("Hello", name)
# hello("ram")


def add(x,y): # add is my fuction name 
    print(x + y)
add(10,20)

def cube(x):
    print(x**3)
cube(2)
# def add(x,y):
#     print(x+y)
# add(10,20)

#default or optional parameter
# def user(name, age):
#     print(f"Name : {name}, Age :{age}")
# user("Ram", "35")


# function accept any number of arguments
# def users(data):
#     print(data)
# users(['RAM', 'sita'])



# Types of argument


# 2. Keyword argument

# 1. Arbitary argument  # Tuple return 
#*args can be used when you don't know how many argument will come from the user
def my_function(*student):
    print("The topper of the class is " + student[2] )
my_function("ram", "sita", "hari", "krishna")

# 2. Keyword argument
#**kwargs  can be used when we want to pass key value pair data from the user
def my_function(**student):
    print("The topper of the class is " + student['name'] )
my_function(name="ram", age=25, marks=90)

# Default Arguments
# Value assign  in the term of assignment(=) operators of the kwywordname = value
# def function_name (param1, param2 = default_value2)

def my_function(name, age = 25):
    print(name)
    print(age)
my_function("ram")
my_function("sita", 30)

def my_function(country='Nepal'):
    print("The name of the country is " + country)
my_function("India")
my_function()  # if we don't pass the argument then it will print the default value



# 3. Default argument


# function return value # stops the execution of the function that returns callable item and it can be stored in a variables
def add (a,b):
    return a + b
print(add(10,20))

# def add(x,y):
#     return x +y
# print(add(4,6))


# function scope
#1.Local scope
#2. Global scope

# Pattern Recognition 

# Prime number
num = int(input("Enter the number:"))
for x in range(2,num):
    if num%x ==0:
        print(num,"is not a prime number")
        break
else:
    print(num,"is a prime number")

# reverse
num = 171
x = num
rev = 0
while num>0:
    rev = (rev*10) + num%10
    num = num//10
if rev ==x:
    print("palindrome")
else:
    print("not a palindrome")

number = [1,2,1]

copy_number = number.copy()
number.reverse
    
# factorial using recursive function
def fact(n):
    if n == 1 or n==0:
        return 1
    else:
        return n*fact(n-1)
number = int(input("Enter a number:"))
if number<0:
    print("factorial of negative number doesn't exist")
if number>0:
    print(f'factorial of {number} is {fact(number)}')
