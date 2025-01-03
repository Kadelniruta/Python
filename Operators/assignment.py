# Assignment operators : = , +=, -=, *=, /=, %=, **=, //=
# a= 5
# a+=5
# print(a)
# # Output: 10
# b=3
# c=2
# d=7
# e="Hello"
# f=e+" World"
# g=e*4
# h=d**2
# print(f)
# print(g)

#Comparison operators : ==, !=, >, < , >=, <=

# print(5==6)
# print(5<=6)
# print(5>=6)

#Logical operators
# and , or and not
# print(5==5 and 6==6)
# print(5==5 or 6==7)
# print(not (5==6))


#Identity is, is not
# a=5
# b=5
# c=6
# print(a is b)
# print(a is not c)

#Membership operator in, not in
# x=[1,2,3]
# y={1,2,3}
# z="1"
# print(1 in x)
# print(1 in y)
# print("1" in z)

#bitwise operators 
# print(5&6)
# print(bin(5))
# print(bin(6))
# print(bin(4))


#Write a program to enter two number and calculate
# the sum of both numbers.
# num1= 10
# num2 = 5
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num1%num2)
# print(num1**num2)
# print(num1//num2)

#addition, subtraction, multiplication, division
#modulas, floor division, exponentiation

#assign the 10 number
# num1 +=10
# num1 -=10
# num1 *=10
# num1 /=10
# num1 %=10
# num1 **=10
# num1 //=10
# print(num1)

# num2 +=10
# num2 -=10
# num2 *=10
# num2 /=10
# num2 **=10
# num2//=10
# num2 %=10

# # and or not

# print(10==5 and 5==10)
# print(10==5 or 5==3)
# print(not(5==10 and 10==5))

# #Comparison
# x = 10
# y = 5
# print(x==y)
# print(x!=y)
# print(x>y)
# print(x<y)
# print(x>=y)
# print(x<=y)


# #Identity Operators
# #a is b #checks if both variables point to the same object.
# a=5
# b=6
# c=b
# print(a is not b)
# print(a is c)

# #Membership Oerators
# x={1,2,3}
# y={3,1,7}
# print(1 in x)
# print(4 not in y)

# Condition 

# a = 5
# b = 50

# if a>b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# if a > b :
#     print("a is greater than b")

# else:
#     print("b is greater than a")


#even or odd
# number = int(input("Enter the first num: "))
# if number%2 ==0:
#     print("The number is even")
# else:
#     print("The number is odd")


# num = int(input("Enter the number: "))
# if num%3 ==0 and num%5 ==0:
#     print("The number is divisible by 5 and 3.")
# else:
#     print("The number is not divisible ny 5 and 3: ")

# a=5
# b=6
# c=10

# if a>b and a>c:
#     print("a is greater than both of them")
    
# elif b>a and b>c:
#     print("b is greater than both of them")
# elif a==b and b==c:
#     print("All are equal")
    
# else:
#     print("c is greater than both of two.")



# a=6
# b=6
# c=10

# if a>b and a>c:
#     print("a is greater than both of them")
    
# elif b>a and b>c:
#     print("b is greater than both of them")
# elif a==b or b==c:
#     print("All are equal")
    
# else:
#     print("c is greater than both of two.")


#Write a program to enter username and password
# user_name = input('Please Enter your Username : ')
# password = input('Please Enter your Password : ')

# if user_name =='admin' and password=="admin":
#     print ("Login Successful")
# else:
#     print ("Invalid. Please try again.")


#WAP to enter five subject marks and fina the total, percentage and division
# oop = int(input("Enter Marks for OOP : "))
# mysql = int(input("Enter Marks for DBMS : "))
# os = int(input("Enter Marks for OS : "))
# ai = int(input("Enter Marks for AI : "))
# database= int(input("Enter Marks for Database: "))

# total_marks = oop + mysql + os + ai + database
# print(f"The total marks is:  {total_marks}")
# percentage = (total_marks/500) *100
# print(f"The percentages is:  {percentage}")

# if percentage>85 and percentage<=100:
#     print("Your division is A+")
# elif percentage>60 and percentage<=85:
#     print("Your division is A")
# elif percentage>40 and percentage<=60:
#     print("Your division is B+")
# else:
#     print("Your division is c")

# write a program for ascending 
# a= int(input("Enter a: "))
# b=int(input("Enter b: "))
# c = int(input("Enter c:"))

# if a>b and a>c:
# #     print
# age = int(input("Enter the age:"))
# if age<18:
#     print("child")

# elif  age>40:
#     print("old")

# else:
#     print("welcome")
#     if age>18 and age<=25:
#         print("Coke")
#     elif age>25 and age<=30:
#         print("Beer")
#     else:
#         print("All items")

# age = int(input("Enter the age: "))
# if age<18:
#     print("not eligible")
# elif age>=18 and age<=40:
#     print("eligible")
#     if age>18 and age<25:
#         print("You can drink")

#Write a program for atm

print("Welcome to the ATM. ")

pin =(int(input("Enter the pin: ")))
if pin==1234:
    balance=10000
    print("Welcome")
    print("1. Withdraw")
    print("2. Balance Enquiry")

    option = int(input("Enter option: "))
    if option==1:
        amount = int(input("Enter a amount:"))
        if amount<=balance:
            print("Collect Cash....")
            rem = balance-amount
            print("Rem: amount: ", rem)
        else:
            print("insufficient balance")
    elif option==2:
         print("Balance is : ", balance)
    else:
        print("Invalid option")

    
else:
    print("Invalid Pin")
  





















