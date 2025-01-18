# class Car:
#     color='black'

#     @staticmethod
#     def start():
#         print('start')

# class Tata(Car):
#     def __init__(self,model):
#         self.model=model

# t1 = Tata('tiago')
# print(t1.model,t1.color)
# t1.start()
      
# Multilevel inheritance
class Car:
    category = "electric"
    @staticmethod
    def start():
        print('car starts')

    @staticmethod
    def stop():
        print('car stops')
    
class Ford(Car):
    def __init__(self,model):
        
        self.model = model

class Figo(Ford):
        def __init__(self,price):
            self.price = price

f1 = Figo(19000)
print(f1.price)

f1.start()
f1.stop()

# Multiple Inheritance
class A:
     a1 = 'hi everyone'

class B:
     b1 = 'hello'

class c(A,B):
     c1 = 'is everything all good?'

c2 = c()
print(c2.a1)
print(c2.b1)
print(c2.c1)

# Hierachial inheritance?
class Animal:
     def speak(self):
          print('animal speaks')

class Dog(Animal):
     def speak(self):
          return "barks"
class Cat(Animal):
     def speak(self):
          return "meow"
class Cow(Animal):
     def speak(self):
          return "moo"
dog = Dog()
cat = Cat()
cow = Cow()
print(dog.speak())
print(cat.speak())
print(cow.speak())

# Super Method
#%%
class Student:
     def __init__(self,name,id):
          self.name = name
          self.id = id
class IIMS(Student):
     def __init__(self,name,id,marks):
          super().__init__(name,id)
          self.marks = marks
i1 = IIMS('Rahul',123,90)
print(i1.name)
print(i1.id)
print(i1.marks)


# Create a class employee with attributes name and salary using instance method. 
# then create a child class called 'fusem' and create its own attribute experience.then inherit the propeties of parent class using super() function
class Employee:
     def __init__(self,name,salary):
          self.name = name
          self.salary = salary
class Fusem(Employee):
     def __init__(self,name,salary,experience):
          super().__init__(name,salary)
          self.experience = experience
f1 = Fusem('Niru',50000,5)
print(f1.name)
print(f1.salary)
print(f1.experience)


# %%
