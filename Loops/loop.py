# numbers = [1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     if num ==3:
#         print("Found!")
#         # break
#         # continue
#     print(num)

# x =1
# while x <=10:
#     print(x)
#     x += 1


# a =1
# while a<=10:
#     print("Niruta Kadel")
#     a+=1


# a =10
# while a >=1:
#     print(a)
#     a -= 1

#even number 
# b = 1

# while b <=10:
#     b+=1
#     if b % 2 == 0 :
#         print(b)


#sum of 10 number is 55 in while loop

# x=1
# sum =0
# while x <=10:
#     sum += x
#     x += 1
# print("The sum of first 10 natural numbers is ",sum)


#multiplication of 2 table using for loop

# x=0
# product = 0
# while x<=9:
#     product+=2
#     x+=1
#     print(f"2*{x}={product}")

# i = 1
# while i<=10:
#     print(f"2 x {i} = {2*i}")
#     i+=1

# i = 1
# num = int(input("Enter the number: "))
# while i<=10:
#     print(f"{num}x {i} = {num*i}")
#     i+=1


# data = [12,44,88,99]
# a=0
# while a<len(data):
#     print(data[a])
#     a+=1


#what is loop?
#A loop is a programming construct that allows code to be executed repeatedly. 
# It is used when we
#types of loop
#1. for loop: sequential loop
#2. while loop:  it checks the condition before executing the statements in the loop.
#3.  nested loops: one loop can be inside another loop.
#for loop example
# for i in range(5):
#     print(i)

#for loop syntax
#for variable_name in sequence (iterable object):
#statements

  
# data = [23,56,78,98,79]
# for num in data:
#     print(num)

# name = "Python"
# for letter in name:
#     print(letter)
# for x in range(10):
#     print(x)


# for x in range(1,11,2):
#     print(x,end=',')


# data = [23,56,78,98,79]
# total = len(data)
# for i in range(total):
#     print(data[i])

# data = [23,56,78,98,79]
# for x in data:
#     if x==56 or x==98:
#         print(x)

# data = [23,56,78,98,79,56,88,100]
# sum =0
# for x in data:
   
#     sum = sum +x
#     if x%2!=0:
#         print(x)
# print(sum)


# data=[]
# num = int(input("Enter the number of elements: "))
# for x in range(num):
#     name = input("Enter the name: ")
#     data.append(name)
# for name in data:
#     print("Your entered:  ",name, end=',')
    


# data =[]

# num  = int(input("How many numbers you want to enter? "))
# for i in range(num):
#     n = int(input("Enter a number :"))
#     if n not in data:
#         data.append(n)
# for num in data:
#     #not repeated number
#    print(num)

#nested loop

# for x in range(1,4):
#     print(f".......{x}........")
#     for y in range(1,6):
#         print(y,end="\t")
#     print()

# for x in range(1,6):
#     for y in range(1,11):
#         z=x*y
#         print(f"{x} x {y}= {z}")
       
#     print()



#number of student
#5 subject enter marks
#total
#percentages
#division


# number_student = int(input("Enter the number of student: "))
# current_student = 1

# while  current_student <= number_student:
#     print(f"Student {current_student}: ")

# total_marks = 0
# number_student = 5

# for subject in range(1, number_student+1):
#     marks = float(input(f"Enter Marks in Subject {subject}: "))
#     total_marks += marks

# total = total_marks
# percentage = (total / (number_student*100)) * 100

# #determine the division based on percentages
# if percentage>=75:
#     print(f"Division : Distinction ")

# elif percentage>=60 :
#     print(f"Division : First Division ")

# elif percentage>=45 :
#     print(f"Division : Second Division ")

# elif percentage>=35 :
#     print(f"Division : Third Division ")

# else:
#     print("Division : Fail")



# print(f"Total marks: {total}")
# print(f"Percentage: {percentage}%")

# current_student +=1


# num_students = int(input("Enter the number of students: "))

# for x in range(num_students):
#     oop = int(input("Enter Marks for OOP : "))
#     mysql = int(input("Enter Marks for DBMS : "))
#     os = int(input("Enter Marks for OS : "))
#     ai = int(input("Enter Marks for AI : "))
#     database= int(input("Enter Marks for Database: "))
#     total = oop + mysql + os + ai + database
#     average = total/5
#     percentage = (total /500) * 100
#     print(f"The total marks is : {total}")
#     print(f"The  average mark is :{average} ")
#     print(f"The percentages is : {percentage}%")

#     if percentage>85 and percentage<=100:
#      print("Your division is A+")
#     elif percentage>60 and percentage<=85:
#         print("Your division is A")
#     elif percentage>40 and percentage<=60:
#         print("Your division is B+")
#     else:
#         print("Your division is c")



# data = [
#     {'name': 'ram', 'address':'bkt'},
#     {'name': 'shyam','address':'dhaka'},
#     ]
# # print(data[0]['name'])

# for user in data:
#     print(user['name'],'is living at',user['address'])


# users =[
#     {'name':"ram", 'gender':"male", 'status' : True},
#     {'name':"sita", 'gender':"Female", 'status' : False},
#     {'name':"hari", 'gender':"male", 'status' : False},
#     {'name':"laxmi", 'gender':"Female", 'status' : True}

# ]

# #write a program to find total user
# total_users = len(users)
# print(f"Total number of users are : {total_users}")

# #Total male
# male_user = 0
# female_user=0
# total_active=0
# total_inactive=0

# for user in users:
#     if user["gender"] == "male":
#         male_user += 1
#     else:
#         female_user+=1
    
#     if user["status"] == True:
#         total_active +=1
#     else:
#         total_inactive +=1
# print(f"Number of Male Users are : {male_user}")
# print(f"Number of Female Users are : {female_user}")
# print(f"Number of active users are: {total_active}")
# print(f"Number of Inactive users are: {total_inactive}")
    
# name = input("Enter the user name: ")
# not_found = True
# for user in users:
#     if user['name'] == name:
#         print(user)
#         not_found=False
# if not_found:
#     print("user not found")



# data =[
#     [12,34,56,78],
#     [87,99,67,87]
# ]


# sums = [0] * len(data[0])
# for num in data:
#     for i in range(len(num)):
#         sums[i] += num[i]
# print(f"The sum  of each column is as follows:\n{sums}")


# for i in range(len(data[0])):
#     sum_result=data[0][i] + data[1][i]
#     print(f"{data[0][i]} + {data[1][i] } = {sum_result }")

# a = 0
# while a<=10:
#     a+=1
#     if a == 5:
#         continue
#     print(a)


# i =0
# while i<=10:
#     i+=1
#     if i==3 or i==5 or i==9:
#         continue
#     print(i)


# lang = 'nepali'

# match(lang):
#     case 'nepali':
#         print("Nepali Language")
#     case 'english':
#         print('English')
#     case _:
#         print('Unknown language')

#no of employee
#name 
#max_salary = 50000
#min_salary = 10000
#role: frontend as 0 and Backend as 1
#find the no of employee at frontend and no of employee at backend





# print(".......ABC Company........")
# emp = int(input("Number of employee: "))
# salary = []
# increment = 1
# frontend =0
# backend =1
# min_salary = 10000
# max_salary = 50000
# while increment<=emp:
#     print(f".....Employee:{increment}......")
#     for i in range(1):
#         name = input("Enter the name of the employee: ")
#     increment+=1
# for employee in name :
#     role = int(input("Enter the role 1.Forntend and 2. Backend: " ))
#     salary =int(input("Enter the salary of the employee: "))
#     if min_salary <=employee["salary"]<=max_salary:
#         if employee["role"]==0:
#             frontend+=1
#         elif employee["role"] ==1:
#             backend +=1
# print("Number of employee in Frontend :",{frontend})
# print("Number of employee in Backend :",{backend})
    



# print("=============ABC==============")
# num = int(input("number of students: "))
# increment=1
# students_marks=[]

# while increment<=num:
#     print(f"=========Student:{increment}============= ")
#     for a in range(1):
#         nep = int(input("Enter nep mark: "))
#         eng = int(input("Enter eng mark: "))
#         mat = int(input("Enter mat mark: "))
#         sic = int(input("Enter sic mark: "))
#         pop = int(input("Enter pop mark: "))
#         total = nep+eng+mat+sic+pop
#         students_marks.append(total)

#     increment+=1



# print("=============RESULT==============")
# s_id=1
# for mark in students_marks:
#     per = mark/5
#     grade =""
#     if per>35 and per<=45:
#         grade="D"
#     elif per>45 and per<=60:
#         grade="C"
#     elif per>60 and per<=80:
#         grade="B"
#     elif per>80:
#         grade="A"
#     else:
#         print("Grade: D")
#     print(f"Student {s_id} got {mark} marks and {per} percentage and grade {grade}")
#     s_id+=1




#no of employee
#name 
#max_salary = 50000
#min_salary = 10000
#role: frontend as 0 and Backend as 1
#find the no of employee at frontend and no of employee at backend

# print("===========Employee Record===========")

# num = int(input("Enter the number of employee: "))
# emp_details=[]
# salary_range=[10000,20000,30000,40000,50000]
# role_range=[0,1]

# x=1

# while x <= num :
#     for a in range(1):
#         name =input("Enter the name: ")
#         salary =int(input("Enter the salary: "))
#         if not salary in salary_range:
#             print("Invalid Salary")
#             exit()
#         else: 
#             role = int(input("Enter the role (FrontEnd-0,BackEnd-1" ,"\nPress Enter to continue"))
#             if not role in role_range:
#                 print("Invalid Role")
#             data ={
#             "name": name,
#             "salary": salary,
#             "role": role
#         }
#             emp_details.append(data)
#     x +=1
# print("==========Employee Details==========")
# print("Sn, Name , Salary, Role")
# x=1
# for emp in emp_details:
#     print(f"{x}, {emp['name']} , {emp['salary']} , {emp['role']} )")
#     x+=1
#     if role==0:
#         print("Frontend")
#     else:
#         print("Backend")


    


#1
#2 2
# 3 3 3
#4 4 4 4
# 5 5 5 5 5

# for i in range(1,6):
#     for x in range(1, i+1):
#         print(i,end="")
#     print()
 
# for i in range(1,6):
#     for x in range(i-1,5):
#         print("*", end="")
#     print()


 
print("=======Welcome to Library========")












