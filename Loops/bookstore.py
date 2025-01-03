print("========Welcome=======")
users = [
    {"username":"admin","password":"admin"},
    {"username":"niru","password":"niru"},
    {"username":"sophia","password":"sophia"}
]

books=[
    { "title": "The Alchemist", "author": "Paulo Coelho", "price":10},
    { "title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "price":25},
    { "title": "The Catcher in the Rye", "author": "J.D. Salinger", "price":50},
    { "title": "The Secret", "author": "Rhonda Byrne", "price":60}

]
# for user in users:
#     user_name = input("Enter the user name: ")
#     password = input("Enter the password: ")
#     if user.get("username") == user_name or user.get("password")==password:
#         print("Your login was successful please enter the book you want to access")
#     for book in books:
#         title=input("Enter the title of the book you want to access: ")
#         if book.get("title")==title:
#             print("Book Details:")
#             print("Title:", book["title"])
#             print("Author:", book["author"])
#             print("Price:", book["price"])
#             break
#         else:
#             print("You preferred book is not here")
#     else:
#         print("Invalid Login!")

username =input("Enter username: ")
password =input("Enter Password : ")
is_login =False
for user in users:
    if user['username'] == username and user['password'] == password:
        is_login = True
    
        print("title,,author,price")
        for book in books:
            print(f"{book['title']},{book['author']},{book['price']}")
if not is_login:
    print(f"Username or Password is incorrect.") 


