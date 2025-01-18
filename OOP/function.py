a = 'abc'
print(type(a))

# Common higer order function
# map() - applies a given function to each item of an iterable (like list, tuple, dic, string)
# filter() - constructs an iterator from elements of an iterable for which a function returns true
# reduce() - applies a rolling computation to sequential pairs of values in a list

#iterable
# It allows us to access items one after another in a sequence
def fact(n):
    return n * fact(n-1) if n > 1 else 1
numbers =[1,2,3,4,5,6,7,8]

mapped_items = map(fact, numbers)
print(list(mapped_items))


    
# filter : higher order function
# return true or false for either values
# %%
def odd(x):
    return True if x%2 == 0 else False

numbers= [ 1,2,3,4,5,6,7,8,9,10]
filtered_items = filter(odd, numbers)
print(list(filtered_items))
    
# Reduce : it applies the input function to elements of iterable and reduce it into a single value
# %%
from functools import reduce
def get_product(num1,num2):
    return num1 * num2
numbers = [1,2,3,4,5]
product = reduce(get_product,numbers)   
print(product)


 


# list comprehension

# %%
numbers = [1,2,3,4,5]
squares = [x**2 for x in numbers]
print(squares)

a = [x**2 for x in range(1,11)]
print(a)

# Dictionary comprehension
# %%
numbers = [1,2,3,4,5]
squares = {x:x**2 for x in numbers}
print(squares)

# %%
a = {x:x**2 for x in range(1,6)}
print(a)


# make a list of all numbers
# divided by 2 from(1,40)
# %%
numbers = [x/2 for x in range(1,41)]
print(numbers)


# iterator and generator
# allows us to access one after another. example: list, tuple,  dict, strings
# generator: allows us to access one after another but we can't access the whole list at once
# example: generator expression, yield

# iterator = objects that allows you to tranverse through a sequence of data like strings, lists etc.
# It is implemented using iterator protocol:
# 1. __iter__() : returns the iterator object itself. it is requird to make object iterable.
# 2. __next__() : returns the next value from the iterator. After items are finished it raises StopIteration operation


# %%
l1 = [1,2,3,4,5]
my_iterator= iter(l1)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# print(next(my_iterator)) # this will raise StopIteration



# Custom 
# %%
class MyIterator:
    def __init__(self, current, end):
        self.current = current
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration
my_iterator = MyIterator(1, 10)
for i in my_iterator:
    print(i)


# Generator
# It can be used for Loop. 
# Special type of iterators that doesnot use __iter__ and __next__ methods. 
# Instead it uses yield keyword to produce a series of values.
# Generator is a function that returns an iterator.

# yield pauses the execution
# return stop the execution

# Key features of generators:
# 1. Yield Keyword : 
# 2. Memory Efficiency
# 3. Infinite sequence

# allow us to access one after another but we can't access the whole list at once. 
# %%
def my_generator():
   yield 1
   yield 2
   yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))


# %%
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for n in infinite_sequence():
    print(n)





# %%
numerator = int(input("Numerator:"))
denominator = int(input("Denominator:"))
try:
    result = numerator / denominator
    print(result)
except:
    print("Error: Division by zero is not allowed")

# %%


