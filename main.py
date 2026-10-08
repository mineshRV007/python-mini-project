# Import datetime to display the current date on the bill
from datetime import datetime


# List to store all shopping items
cart = []


# Function to add a new item to the cart
def add_item():
    print("\n========== ADD ITEM ==========")

    # Get item name and remove unnecessary spaces
    item_name = input("Enter item name: ").strip()

    # Check whether item name is empty
    if item_name == "":
        print("Item name cannot be empty!")
        return

    # Get and validate quantity
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0!")
            return

    except ValueError:
        print("Invalid input! Quantity must be a number.")
        return

    # Get and validate price
    try:
        price = float(input("Enter price per unit: ₹"))

        if price <= 0:
            print("Price must be greater than 0!")
            return

    except ValueError:
        print("Invalid input! Price must be a number.")
        return

    # Calculate total price of the item
    total = quantity * price

    # Store item details in a dictionary
    item = {
        "name": item_name,
        "quantity": quantity,
        "price": price,
        "total": total
    }

    # Add the item to the cart
    cart.append(item)

    print(f"\n{item_name} added successfully!")
    print(f"Item Total: ₹{total:.2f}")


# Function to display all items currently in the cart
def view_cart():
    print("\n================================================")
    print("                  SHOPPING CART")
    print("================================================")

    # Check whether cart is empty
    if len(cart) == 0:
        print("Cart is empty.")
        print("================================================")
        return

    # Display table headings
    print(f"{'Item':<18}{'Qty':<8}{'Price':<12}{'Total':<12}")
    print("------------------------------------------------")

    # Display every item in the cart
    for item in cart:
        print(
            f"{item['name']:<18}"
            f"{item['quantity']:<8}"
            f"₹{item['price']:<11.2f}"
            f"₹{item['total']:<11.2f}"
        )

    print("================================================")


# Function to calculate the subtotal of all items
def calculate_subtotal():
    subtotal = 0

    # Add the total price of every item
    for item in cart:
        subtotal += item["total"]

    return subtotal


# Function to calculate discount based on subtotal
def calculate_discount(subtotal):
    # No discount below ₹500
    if subtotal < 500:
        discount_rate = 0

    # 5% discount from ₹500 to ₹999.99
    elif subtotal < 1000:
        discount_rate = 5

    # 10% discount for ₹1000 or more
    else:
        discount_rate = 10

    # Calculate discount amount
    discount_amount = subtotal * discount_rate / 100

    return discount_rate, discount_amount


# Function to generate the final bill
def generate_bill():
    print("\n================================================")
    print("                 GENERATE BILL")
    print("================================================")

    # Check whether cart is empty
    if len(cart) == 0:
        print("Cart is empty. Please add items first.")
        print("================================================")
        return

    # Get the current date
    current_date = datetime.now().strftime("%d-%m-%Y")

    # Calculate subtotal
    subtotal = calculate_subtotal()

    # Calculate discount
    discount_rate, discount_amount = calculate_discount(subtotal)

    # Calculate final amount
    grand_total = subtotal - discount_amount

    # Display shop bill heading
    print("              ABC GENERAL STORE")
    print("================================================")
    print(f"Date: {current_date}")
    print()

    # Display bill headings
    print(f"{'Item':<18}{'Qty':<8}{'Price':<12}{'Amount':<12}")
    print("------------------------------------------------")

    # Display each item
    for item in cart:
        print(
            f"{item['name']:<18}"
            f"{item['quantity']:<8}"
            f"₹{item['price']:<11.2f}"
            f"₹{item['total']:<11.2f}"
        )

    print("------------------------------------------------")

    # Display subtotal
    print(f"{'Subtotal:':<38}₹{subtotal:.2f}")

    # Display discount
    print(
        f"{'Discount (' + str(discount_rate) + '%):':<38}"
        f"₹{discount_amount:.2f}"
    )

    print("------------------------------------------------")

    # Display final bill amount
    print(f"{'Grand Total:':<38}₹{grand_total:.2f}")

    print("================================================")
    print("          THANK YOU FOR SHOPPING!")
    print("================================================")


# Function to clear all items from the cart
def clear_cart():
    print("\n========== CLEAR CART ==========")

    # Check whether cart is already empty
    if len(cart) == 0:
        print("Cart is already empty.")
        return

    # Ask the user for confirmation
    confirmation = input(
        "Are you sure you want to clear the cart? (y/n): "
    ).lower()

    # Clear the cart if user confirms
    if confirmation == "y":
        cart.clear()
        print("Cart cleared successfully!")

    elif confirmation == "n":
        print("Cart was not cleared.")

    else:
        print("Invalid choice. Cart was not cleared.")


# Main program
while True:
    # Display the main menu
    print("\n========================================")
    print("       SHOPPING BILL GENERATOR")
    print("========================================")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Generate Bill")
    print("4. Clear Cart")
    print("5. Exit")
    print("========================================")
    # Get user's menu choice
    choice = input("Enter your choice: ")

    # Execute the selected operation
    if choice == "1":
        add_item()

    elif choice == "2":
        view_cart()

    elif choice == "3":
        generate_bill()

    elif choice == "4":
        clear_cart()

    elif choice == "5":
        print("\nThank you for using Shopping Bill Generator!")
        print("Program ended.")
        break
    else:
        print("\nInvalid choice! Please select a number from 1 to 5.")