# Write a method to add complex number:
# 3i + 4j
# 5i + 7j
# Output: 8i + 11j

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    def __str__(self):
        return f"{self.real}i + {self.imag}j"
    
# Method to add complex number
def add_complex_number(num1, num2):
    return num1 + num2

num1 = ComplexNumber(3,4)
num2 = ComplexNumber(5,7)
print(add_complex_number(num1, num2)) 


# Getter and setter methods
# %%
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @name.setter
    def name(self, value):
        self.__name = value
    @age.setter
    def age(self,value):
        self.__age = value
    
p1 = Person("Niru",22)
print(p1.name)

print(p1.age)
p1.name = "Niru123"
print(p1.name)
p1.age = 25
print(p1.age)

    
