# data = ['php', 'python', 'java', 'c++']
# course_name = input("Enter the course name: ")
# if course_name in data:
#     print("Course is avaiable")
# else:
#     print("Course is not avaiable")

users = {
    'username':"admin",
    'password': "admin123"
}
user_name = input("Enter the username: ")
password = input("Enter the password: ")

if user_name==users['username'] and password==users['password']:
    print("You are logged in")
else:
    print("Invalid")
