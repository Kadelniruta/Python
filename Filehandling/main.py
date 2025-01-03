#What is file handling?
#File Handling is a programming technique in which we can interact with files. It allows us to create
#open()
#File name
#R-read
# w-write
# a - append
# r+- read and write

#types of files: text and binary?

# handle = open("filehandling/users.txt", "a")  # Open the file 'filehandling.py
# handle.write("ram")
# handle.write("\n")
# handle.write("Niru")
# handle.close( )                      # Close the file after writing

# name, email, address, phone? write a code inform of file handling?

# name= input("Enter the name: ")
# email = input("Enter the email: ")
# address = input("Enter the address: ")
# phone = int(input("Enter the phone number: "))

# handle = open("filehandling/users.txt","a")   #Opening the file
  
# handle.write(f"Name : {name}\nEmail :{email}\nAddress : {address}\nPhone Number : {phone}" ,'\n)
# handle.close()

# fdata = open(r"filehandling\users.txt", "r")    # Reading from the file?
# print(fdata.read())
# print(fdata.readline())
# print(fdata.readlines())




print("====================Student Information System=====================")
print("1.Add User")
print("2. View User")
print("3.Search User")

option = int(input("Enter the option: "))
if option == 1:
    handle = open("filehandling\\users.txt", "a")    # Write mode is used to create or
    name = input("Enter the name: ")                # add data in the existing file.
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    handle.write(f"{name} {email} {address}")
    handle.write("\n")
    print("User added successfully!")
elif option ==2:
    print("Name\tEmail\tAddress")
    handle=open('filehandling/users.txt','r')     
    for line in handle:
        print(line)
    handle.close()

elif option ==3:
    search= input("Enter the name to search: ")
    handle = open("filehandling/users.txt",'r')
    for line in handle:
        if search in line:
            print(line)
else:
    print("Invalid Option")




