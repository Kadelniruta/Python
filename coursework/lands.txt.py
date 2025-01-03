import datetime
import os

# Define a class to represent a land
class Land:
    def __init__(self, kitta_number, city, direction, area, price, status):
        self.kitta_number = kitta_number
        self.city = city
        self.direction = direction
        self.area = area
        self.price = price
        self.status = status

# Define a class to represent a customer
class Customer:
    def __init__(self, name):
        self.name = name

# Define a function to read the land data from the text file
def read_land_data(file_name):
    lands = []
    with open(file_name, 'r') as f:
        for line in f:
            kitta_number, city, direction, area, price, status = line.strip().split(',')
            lands.append(Land(kitta_number, city, direction, int(area), int(price), status.strip()))
    return lands

# Define a function to display the available lands
def display_available_lands(lands):
    print("Available Lands:")
    for land in lands:
        if land.status == "Available":
            print(f"Kitta Number: {land.kitta_number}, City: {land.city}, Direction: {land.direction}, Area: {land.area} annas, Price: {land.price} NPR")

# Define a function to validate input data
def validate_input(prompt, data_type):
    while True:
        user_input = input(prompt)
        if data_type == int:
            try:
                return int(user_input)
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        elif data_type == str:
            return user_input

# Define a function to rent a land
def rent_land(lands, customer, kitta_number, duration):
    for land in lands:
        if land.kitta_number == kitta_number and land.status == "Available":
            land.status = "Not Available"
            generate_rent_note(customer, land, duration)
            return
    print("Land not available for rent.")

# Define a function to return a land
def return_land(lands, customer, kitta_number):
    for land in lands:
        if land.kitta_number == kitta_number and land.status == "Not Available":
            land.status = "Available"
            generate_return_note(customer, land)
            return
    print("Land not returned.")

# Define a function to generate a rent note
def generate_rent_note(customer, land, duration):
    note_file_name = f"Rent_Note_{customer.name}_{land.kitta_number}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(note_file_name, 'w') as f:
        f.write(f"Kitta Number: {land.kitta_number}\n")
        f.write(f"City: {land.city}\n")
        f.write(f"Direction: {land.direction}\n")
        f.write(f"Area: {land.area} annas\n")
        f.write(f"Customer: {customer.name}\n")
        f.write(f"Date and Time of Rent: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Duration of Rent: {duration} months\n")
        f.write(f"Total Amount: {land.price * duration} NPR\n")

# Define a function to generate a return note
def generate_return_note(customer, land):
    note_file_name = f"Return_Note_{customer.name}_{land.kitta_number}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(note_file_name, 'w') as f:
        f.write(f"Kitta Number: {land.kitta_number}\n")
        f.write(f"City: {land.city}\n")
        f.write(f"Direction: {land.direction}\n")
        f.write(f"Area: {land.area} annas\n")
        f.write(f"Customer: {customer.name}\n")
        f.write(f"Date and Time of Return: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# Main function
def main():
    lands = read_land_data("lands.txt")
    display_available_lands(lands)
    while True:
        user_choice = validate_input("Enter your choice (1 - Rent Land, 2 - Return Land, 3 - Quit): ", int)
        if user_choice == 1:
            customer_name = validate_input("Enter customer name: ", str)
            customer = Customer(customer_name)
            kitta_number = validate_input("Enter kitta number: ", int)
            duration = validate_input("Enter duration of rent in months: ", int)
            rent_land(lands, customer, kitta_number, duration)
        elif user_choice == 2:
            customer_name = validate_input("Enter customer name: ", str)
            customer = Customer(customer_name)
            kitta_number = validate_input("Enter kitta number: ", int)
            return_land(lands, customer, kitta_number)
        elif user_choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()