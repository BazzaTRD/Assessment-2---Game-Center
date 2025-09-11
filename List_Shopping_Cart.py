#Sanjith Padmadas Das 8/28/2025 3:40 PM • # CRUD - Create/Read/Update/Delete
# 🛒 Shopping Cart Application

# Lists to store product names and prices
cart = []
prices = []

#list of products and their corresponding weight
products = ["banana","blueberry","apple","blackberry", "strawberry"]
product_price = [3.99, 12.49, 3.50, 5.50, 6.99]
product_all = zip(products, product_price)



# function to view available products and and their prices
def view_available_product_price():
    for (product, price) in zip(products, product_price):
        print(product, f"${price}")
    


# Function to add an item to the cart
def add_item():
    name = input("Enter product name: ").strip().lower()
    if name not in products:
        print(f"The item '{name}' does not exist...")
        return
    weight = float(input("Enter how many kg you want: "))
    try:
        price = product_price[products.index(name)] * weight
        cart.append(name)
        prices.append(price)
        print(f"{name} added for ${price:.2f}")

    except ValueError:
        print("Invalid price. Please enter a number.")

# Function to view cart contents
def view_cart():
    if not products:
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
        print("Product has been removed successfrully.")
        return
    try:
        index = int(input("Enter the item number to remove: "))
        if 1 <= index <= len(products):
            removed_item = cart.pop(index - 1)
            prices.pop(index - 1)
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
    print("1. View_Available_Product_Price")
    print("2. Add item")
    print("3. View cart")
    print("4. Remove item")
    print("5. Checkout and Save to File")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice (1–5): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        view_available_product_price()
    if choice == 2:
        add_item()
    elif choice == 3:
        view_cart()
    elif choice == 4:
        remove_item()
    elif choice == 5:
        checkout()
    elif choice == 6:
        print("Thank you for using the Shopping Cart. Goodbye!")
        break
    else:
        print("Please choose a valid option (1–5).")
