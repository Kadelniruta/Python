num = int(input("Enter the number:"))
for x in range(2,num):
    if num%x ==0:
        print(num,"is not a prime number")
        break
else:
    print(num,"is a prime number")