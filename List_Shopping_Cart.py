#Sanjith Padmadas Das 8/28/2025 3:40 PM • # CRUD - Create/Read/Update/Delete
# 🛒 Shopping Cart Application

# Lists to store product names and prices
cart = []
prices = []

# Function to add an item to the cart
def add_item():
    name = input("Enter product name: ").strip()
    try:
        price = float(input("Enter product price: "))
        if price < 0:
            print("Price cannot be negative.")
            return
        cart.append(name)
        prices.append(price)
        print(f"{name} added for ${price:.2f}")
    except ValueError:
        print("Invalid price. Please enter a number.")

# Function to view cart contents
def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print("\nYour cart contains:")
    total = 0
    for i, (item, price) in enumerate(zip(cart, prices), start=1):
        print(f"{i}. {item} - ${price:.2f}")
        total += price
    print(f"Total: ${total:.2f}\n")

# Function to remove an item from the cart
def remove_item():
    view_cart()
    if not cart:
        return
    try:
        index = int(input("Enter the item number to remove: "))
        if 1 <= index <= len(cart):
            removed_item = cart.pop(index - 1)
            removed_price = prices.pop(index - 1)
            print(f"{removed_item} removed from cart.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to checkout and save to file
def checkout():
    if not cart:
        print("Your cart is empty. Nothing to checkout.")
        return
    total = sum(prices)
    print("\nFinal cart:")
    for i, (item, price) in enumerate(zip(cart, prices), start=1):
        print(f"{i}. {item} - ${price:.2f}")
    print(f"Total: ${total:.2f}")
    
    try:
        with open("shopping_cart.txt", "w") as file:
            for item, price in zip(cart, prices):
                file.write(f"{item} - ${price:.2f}\n")
            file.write(f"\nTotal: ${total:.2f}\n")
        print("Order saved to shopping_cart.txt")
    except IOError:
        print("Error saving to file.")

# Main loop
while True:
    print("\nShopping Cart Menu")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Checkout and Save to File")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1–5): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        add_item()
    elif choice == 2:
        view_cart()
    elif choice == 3:
        remove_item()
    elif choice == 4:
        checkout()
    elif choice == 5:
        print("Thank you for using the Shopping Cart. Goodbye!")
        break
    else:
        print("Please choose a valid option (1–5).")
