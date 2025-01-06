# What is variable?
# Variable is a container that store data/values.

     
# x=10 assignment operator
# print(type(x))
# print(id(x))
# print(dir(x))

# a=10
# b=30
# print("Value of a:",a)
# print("Value of b:",b)

# a,b, *c = 10,22,33,56,78,89,56
# print(a,b,c)

user_name ="Niru"
password=123
print(f"Username: ", {user_name})


name="ram"
age = 20
address = "ktm"

print(name)
print(age)
print(address)

# Local Scope # declared inside a function . It can only be accessed within that function.

def my_function():
    var = 10
    print(var)
my_function()

# Global Scope = declared outside any function. It can accessed from any function with in the same module. 

def my_function():
    global var
    var = 10
    print(var)
my_function()
print(var)

# Enclosing Scope(Non-local scope) = Scope of any enclosing function, excluding the global scope. 

def outer_function():
    outer_var = 20

    def inner_function():
        nonlocal outer_var
        outer_var = 30
        print(outer_var)
    inner_function()
outer_function()

# Built-in-scope
# Special variables that are part of the built-in namespace. They are always avaiable in the python.
print(len("Niru")) # 'len' is a built-in function..
print(type(10)) # 'type' is a built-in function...


