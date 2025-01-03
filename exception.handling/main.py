#What is exception handling?
#Is the way to handle error
# That might  occur during program execution.
# print("Exception Handling")
# print(10/0)
# print("Hello")

# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print("An Error Occurred!")
#     print("The error message is :",e)
# print("Hello")

def add(x,y):
    if y==0:
        raise Exception ("Cannot divide by zero.")
    
try:
    print(add(10,9))
except Exception as e :
    print("Caught an exception : ",e)