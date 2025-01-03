# ATM
# print(".....Welcome to the ATM.....")
# pin =int(input("Enter your 4 digits pin: "))
# if pin==1234:
#     balance = 10000
#     print("Correct Pin!")
#     print("1. Withdraw")
#     print("2. Balance Enquiry")
#     option = int(input("Enter a option: "))
#     if option==1:
#         amount=float(input("How much do you want to withdraw? : "))
#         if amount<=balance:
#             print("Collect Cash.....")
#             rem = balance-amount
#             print("Rem Balace : ", rem)
#         else:
#             print("Insufficient Balance.")
#     elif option==2:
#         print("Your Current Balance is Rs.", balance)
#     else:
#         print("Wrong Option Entered.")
        
# else:
#     print("Incorrect Pin.")



#Computer Bazar
# print("...Welcome to the computer bazar...")
# print("1. dell(Rs.20000)")
# print("2. HP (Rs.15000)")
# print("3.MAC(Rs.50000)")
# choice = int(input("Enter Your choice:"))
# if choice==1:
#     qty = int(input("Enter Quantity:"))
#     total_cost = qty*20000 
#     product_name="Dell"

# elif choice == 2:
#     qty = int(input("Enter Quantity:"))
#     total_cost = qty * 15000
#     product_name = "hp"
   
# elif choice==3:
#     qty = int(input("Enter Quantity:"))
#     total_cost= qty * 50000
#     product_name ="Mac"
   
# else:
#     print("Invalid Choice..")

# #Delivery Charge
# delivery_option =  input("Do You Want Delivery?(home/pickup): ")

# if delivery_option == 'home':
#         charge = 1000
# else:
#         charge = 0
    

# #Packing
# packing_type=int(input("Do you want to add any packing material?  Enter 1 for Plastic , 2 for bag and 3 for giftbox: "))
# if packing_type==1:
#      packing_charge = 500
# elif packing_type==2:
#      packing_charge=1000
# elif  packing_type==3:
#      packing_charge=5000
# else:
#      packing_charge = 0

# #city
# city = input("Enter city ( KTM, Bhaktapur and Lalitpur):")
# if city =="KTM":
#      tax_rate = 0.13 #13% vat in kathamndu

# else:
#      tax_rate=0
     

# name =  input("Enter Customer Name : ")
# phone = int(input("Enter the phone number: "))

# print("Your Order Details are as follows: ")
# print(f"Customer name : {name}")
# print(f"Product name : ",{product_name})
# print(f"Phone Number : {phone}")



# net_total = total_cost + charge + packing_charge 
# total_tax_amount = net_total *tax_rate
# print("Total Cost Is:",net_total)
# print("Total tax amount is : ", total_tax_amount)
# final_price = net_total+ total_tax_amount

# print("Your Final Price is Rs.", final_price)


#100min = call duration, gap duration - (0-10)min
#1.ntc to ntc = bonus = 3.5 2. ntc to ncell = bonus = 4.5 , 3. ncell to ncell = bonus = 100 and 4 . ncell to ntc = 2.5


# print("........")
# print("1. ntc to ntc")
# print("2. ntc to ncell")
# print("3. ncell to ncell")
# print("4. ncell to ntc")
# gap_duration = 0

# choice = int(input("Enter the choice: "))
# if choice ==1:
#     bonus = 3.5
#     gap_duration = int(input("Enter the gap duration:"))
    
   
#     if gap_duration>0 and gap_duration<=10:
#         print(f"Bonus: ", bonus)
#     elif gap_duration>10 and gap_duration<=20:
#         print(f"Bonus: ", bonus*2)
#     elif gap_duration>20 and gap_duration<=30:
#         print(f"Bonus: ", bonus*3)
#     elif gap_duration>40 and gap_duration<=50:
#         print(f"Bonus: ", bonus*4)
#     elif gap_duration>60 and gap_duration<=70:
#         print(f"Bonus: ", bonus*5)
#     elif gap_duration>80 and gap_duration<=90:
#         print(f"Bonus: ", bonus*6)
#     elif gap_duration>90 and gap_duration<=100:
#         print(f"Bonus: ", bonus*7)
#     else:
#         print("Your call duration exceeded 100 mins")

# if choice ==2:
#     bonus = 4.5
#     gap_duration = int(input("Enter the gap duration:"))
    
   
#     if gap_duration>0 and gap_duration<=10:
#         print(f"Bonus: ", bonus)
#     elif gap_duration>10 and gap_duration<=20:
#         print(f"Bonus: ", bonus*2)
#     elif gap_duration>20 and gap_duration<=30:
#         print(f"Bonus: ", bonus*3)
#     elif gap_duration>40 and gap_duration<=50:
#         print(f"Bonus: ", bonus*4)
#     elif gap_duration>60 and gap_duration<=70:
#         print(f"Bonus: ", bonus*5)
#     elif gap_duration>80 and gap_duration<=90:
#         print(f"Bonus: ", bonus*6)
#     elif gap_duration>90 and gap_duration<=100:
#         print(f"Bonus: ", bonus*7)
#     else:
#         print("Your call duration exceeded 100 mins")

# if choice ==3:
#     bonus = 10
#     gap_duration = int(input("Enter the gap duration:"))
    
   
#     if gap_duration>0 and gap_duration<=10:
#         print(f"Bonus: ", bonus)
#     elif gap_duration>10 and gap_duration<=20:
#         print(f"Bonus: ", bonus*2)
#     elif gap_duration>20 and gap_duration<=30:
#         print(f"Bonus: ", bonus*3)
#     elif gap_duration>40 and gap_duration<=50:
#         print(f"Bonus: ", bonus*4)
#     elif gap_duration>60 and gap_duration<=70:
#         print(f"Bonus: ", bonus*5)
#     elif gap_duration>80 and gap_duration<=90:
#         print(f"Bonus: ", bonus*6)
#     elif gap_duration>90 and gap_duration<=100:
#         print(f"Bonus: ", bonus*7)
#     else:
#         print("Your call duration exceeded 100 mins")

# if choice ==4:
#     bonus = 2.5
#     gap_duration = int(input("Enter the gap duration:"))
    
   
#     if gap_duration>0 and gap_duration<=10:
#         print(f"Bonus: ", bonus)
#     elif gap_duration>10 and gap_duration<=20:
#         print(f"Bonus: ", bonus*2)
#     elif gap_duration>20 and gap_duration<=30:
#         print(f"Bonus: ", bonus*3)
#     elif gap_duration>40 and gap_duration<=50:
#         print(f"Bonus: ", bonus*4)
#     elif gap_duration>60 and gap_duration<=70:
#         print(f"Bonus: ", bonus*5)
#     elif gap_duration>80 and gap_duration<=90:
#         print(f"Bonus: ", bonus*6)
#     elif gap_duration>90 and gap_duration<=100:
#         print(f"Bonus: ", bonus*7)
#     else:
#         print("Your call duration exceeded 100 mins")

    













    
