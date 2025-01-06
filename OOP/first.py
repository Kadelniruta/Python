# # Let define an objects
# class Student:
#     name='xyz' # class attribute
#     marks = 32

# s1 = Student()
# print(s1.name, s1.marks)

# Instance method = Self parameter used , it reflects the object , modified or access
# first key i.e. Self
# class Animal:
#     name = 'Lion'
#     def __init__(self,name):
#         self.name= name # instance attribute
    
#     def sound(self):
#         print(f'{self.name} roars')

# o1 = Animal('tiger')
# print(o1.name)
# o1.sound() 
      

class rectangle:

    def __init__(self,l,b):
        self.l = l
        self.b = b
    def perimeter(self):
        return 2*(self.l + self.b)
    
r1 = rectangle(3,4)
r1.perimeter()

# Create a class called student and its attributes as name and marks. 
# Take marks of 3 subjects and then create a method to print the average marks of that student.
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks)/len(self.marks)
s1 = Student('Niru', [90,80,70])
print(s1.average())

# Static Methods 
# Method that do not use self keyword.
# It used decorator @staticmethod.
# They can't access class or instance attributes. Generally used for utility purpose

class Car:
    name ='Jaguar'

    @staticmethod 
    def start():
        print('car starts')

    @staticmethod
    def stop():
        print('car stops')
c1 = Car()
c1.start()
c1.stop()

class Mathop:
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def sub(a,b):
        return a-b
    
Mathop.add(5,2)
Mathop.sub(5,2)
        
    
# Class Method   
# Decorator: @classmethod
# It is used to directly modify class's methods or attributes

class Student:
    name='Anuj'

    def __init__(self, name):
        self.name = name

o1=Student('Jivan')
print(o1.name)
print(Student.name)

class student:
    name='Jivan'
    @classmethod
    def change_name(cls,name):
        cls.name = name
        
o1=student()
o1.change_name('Anuj')
print(o1.name)
print(student.name)
        


        
