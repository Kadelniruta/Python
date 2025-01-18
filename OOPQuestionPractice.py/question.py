# 1. Create a class `Rectangle` with attributes `length` and `width`. Add methods to calculate the area and perimeter of the rectangle. 
# Create an object and test these methods.
#%%
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
rect = Rectangle(5,4)
print(f"Area:{rect.area()}")
print(f"Perimeter:{rect.perimeter()}")



# %%
# 2. Create a class `Student` with attributes `name` and `marks`. Add a method to display the
#student's details and another method to check if the student has passed (pass marks = 40).

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display_details(self):
        print(f"Name:{self.name}")
        print(f"Marks:{self.marks}")

    def has_passed(self):
        return self.marks >= 40
           
        

student = Student("Aliza", 80)
print("Student Details:")
student.display_details()

if student.has_passed():
    print(f"{student.name} has passed.")
else:
    print(f"{student.name} has not passed.")

    

# %%
#3. Write a class `BankAccount` with attributes `account_number`, `balance`, and `name`. Implement
#methods to deposit, withdraw, and display the account details. Ensure withdrawal doesn't exceed
#balance.
class BankAccount:
    def __init__(self, account_number, name, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = float(initial_balance)  # Ensure the balance is stored as a float
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}. New balance is {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount} from account {self.account_number}. New balance is {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Current Balance: {self.balance}")


    # Corrected initial balance to be a numeric value
account = BankAccount("123456789", "Niru Kadel", 12000)  # Pass balance as a number
account.deposit(2000)
account.withdraw(5000)
account.withdraw(15000)  # This will show "Insufficient balance."
account.display_account_details()




# 4.  Create a class "Vechicle" with attributes "brand" and "model". 
# Inherit this class to create a "Car" class and add attributes like "number_of_doors" and "fuel_type". 
# Add methods to display details.
# %%
class Vehicle:
    def __init__(self, brand, model):
        """
        Initialize the Vehicle class with brand and model attributes.
        """
        self.brand = brand
        self.model = model

    def display_details(self):
        """
        Display the details of the vehicle.
        """
        print(f"Vehicle Brand: {self.brand}")
        print(f"Vehicle Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, number_of_doors, fuel_type):
        """
        Initialize the Car class, inheriting attributes from Vehicle
        and adding number_of_doors and fuel_type.
        """
        super().__init__(brand, model)  # Call the constructor of the parent class
        self.number_of_doors = number_of_doors
        self.fuel_type = fuel_type

    def display_details(self):
        """
        Display the details of the car, including inherited and additional attributes.
        """
        super().display_details()  # Call the parent class's display_details method
        print(f"Number of Doors: {self.number_of_doors}")
        print(f"Fuel Type: {self.fuel_type}")


car = Car("Toyota", "Corolla", 4, "Petrol")
car.display_details()




# 5. Implement a class `Animal` with a method `sound()` that prints a generic message. Create
# subclasses `Dog` and `Cat` that override the `sound()` method with specific messages. Demonstrate
# polymorphism.
# %%

class Animal:
    def sound(self):
        """
        Print a generic message.
        """
        print("The animal makes a sound.")
        return
class Dog(Animal):
    def sound(self):
        """
        Print a message specific to dogs.
        """
        print("The dog barks.")
        return
class Cat(Animal):
    def sound(self):
        """
        Print a message specific to cats.
        """
        print("The cat meows.")
        return

dog = Dog()
cat = Cat()
dog.sound()
cat.sound()
               

# 6. Create a class `Library` with attributes `books` (a list of books). Add methods to `add_book()`,
# `remove_book()`, and `list_books()`. Test the class by performing all operations.
#%%

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        """
        Add a book to the library.
        """
        if book not in self.books:
            self.books.append(book)
            print(f"Book '{book}' added to the library.")
        else:
            print(f"Book '{book}' is already in the library.")
            
        
    def remove_book(self, book):
        """
        Remove a book from the library.
        """
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed from the library.")
        else:
            print(f"Book '{book}' is not in the library.")
            
           
    def list_books(self):
        """
        List all books in the library.
        """
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f'- {book}')
        else:
            print("No books in the library.")


        
my_library = Library()

    # Adding books
my_library.add_book("1984 by George Orwell")
my_library.add_book("To Kill a Mockingbird by Harper Lee")
my_library.add_book("The Great Gatsby by F. Scott Fitzgerald")

    # Listing books
my_library.list_books()

    # Removing a book
my_library.remove_book("1984 by George Orwell")
    
    # Listing books again
my_library.list_books()

    # Trying to remove a book that doesn't exist
my_library.remove_book("Moby Dick by Herman Melville")

    # Adding a duplicate book
my_library.add_book("To Kill a Mockingbird by Harper Lee")

    # Final list of books
my_library.list_books()

#7. Create a class `Employee` with attributes `name` and `salary`. Add a method to increment the
#salary by a given percentage. Create a few employee objects and test the functionality.

#%%
class Employee:
    def __init__(self, name, salary):
        """Initialize the Employee with a name and salary."""
        self.name = name
        self.salary = salary

    def increment_salary(self, percentage):
        """Increment the salary by a given percentage."""
        if percentage < 0:
            print("Percentage must be a positive value.")
            return
        increment_amount = (percentage / 100) * self.salary
        self.salary += increment_amount
        print(f"{self.name}'s salary has been increased by {percentage}%. New salary: ${self.salary:.2f}")

    def __str__(self):
        """Return a string representation of the Employee."""
        return f"Employee Name: {self.name}, Salary: ${self.salary:.2f}"

# Testing the Employee class

    # Creating employee objects
emp1 = Employee("Niru", 60000)
emp2 = Employee("Sam", 70000)
emp3 = Employee("Yangma", 80000)

    # Displaying initial salaries
print(emp1)
print(emp2)
print(emp3)

    # Incrementing salaries
emp1.increment_salary(10)  # Increase Alice's salary by 10%
emp2.increment_salary(5)    # Increase Bob's salary by 5%
emp3.increment_salary(15)   # Increase Charlie's salary by 15%

    # Displaying updated salaries
print(emp1)
print(emp2)
print(emp3)

#%%   
# 8. Write a program to demonstrate multiple inheritance using a `Person` class and a `Worker` class
# to create a `Teacher` class that inherits from both.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Worker:
    def __init__(self, job_title, salary):
        self.job_title = job_title
        self.salary = salary

    def display_job_info(self):
        return f"Job Title: {self.job_title}, Salary: ${self.salary:.2f}"


class Teacher(Person, Worker):
    def __init__(self, name, age, subject, salary):
        Person.__init__(self, name, age)  # Initialize Person attributes
        Worker.__init__(self, "Teacher", salary)  # Initialize Worker attributes
        self.subject = subject

    def display_teacher_info(self):
        person_info = self.display_info()
        job_info = self.display_job_info()
        return f"{person_info}, Subject: {self.subject}, {job_info}"


# Testing the Teacher class

# Create a Teacher object
teacher = Teacher("John Doe", 30, "Mathematics", 50000)

# Display the teacher's information
print(teacher.display_teacher_info())

#%%

#9. Create a `Calculator` class with methods to add, subtract, multiply, and divide two numbers.
#Handle the division by zero case gracefully.
class Calculator:
    def add(self, a, b):
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of two numbers."""
        return a - b

    def multiply(self, a, b):
        """Return the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of two numbers, handling division by zero."""
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b


# Testing the Calculator class
calculator = Calculator()



    # Test addition
print("Addition (5 + 3):", calculator.add(5, 3))

    # Test subtraction
print("Subtraction (5 - 3):", calculator.subtract(5, 3))

    # Test multiplication
print("Multiplication (5 * 3):", calculator.multiply(5, 3))

    # Test division
print("Division (5 / 3):", calculator.divide(5, 3))
print("Division (5 / 0):", calculator.divide(5, 0))

#%%
# 10. Write a class `Book` with attributes `title`, `author`, and `price`. Add a class-level attribute
# `discount` to apply a discount on the book price. Demonstrate the use of class variables.
class Book:
    # Class-level attribute for discount
    discount = 0.1  # 10% discount

    def __init__(self, title, author, price):
       
        self.title = title
        self.author = author
        self.price = price

    def price_after_discount(self):
        # Calculate the price after applying the class-level discount.
        discounted_price = self.price * (1 - Book.discount)
        return discounted_price

    def __str__(self):
    
        return f"Title: '{self.title}', Author: {self.author}, Price: ${self.price:.2f}, Price after discount: ${self.price_after_discount():.2f}"


# Testing the Book class

    # Create book objects
book1 = Book("1984", "George Orwell", 15.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 12.99)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)

    # Display book information
print(book1)
print(book2)
print(book3)

    # Change the class-level discount
Book.discount = 0.2  # 20% discount

    # Display book information after changing the discount
print("\nAfter changing the discount to 20%:")
print(book1)
print(book2)
print(book3)

        
# %%
