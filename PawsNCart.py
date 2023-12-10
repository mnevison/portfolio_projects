stock_list = [
    {"item": "Cat Food", "price": 4.50},
    {"item": "Dog Food", "price": 4.50},
    {"item": "Dog Toy", "price": 2.50},
    {"item": "Cat Toy", "price": 2.00},
    {"item": "Catnip", "price": 1.50},
    {"item": "Feeding Hay", "price": 3.00},
]

cart = []  
done = False

print("Welcome to Paws n Cart!")
print("\n")

"""
Functionality of the shop. Loops the cart after each option, updates
basket automatically and adds a running total for user to see.

"""

while not done:
    print("-" * 80)
    print("This is your shopping cart")
    total_price = sum(item['price'] * item['quantity'] for item in cart) 
    if cart:
        for item in cart:
            print(f"Item: {item['item']:15} Price: £{item['price']:.2f}\
 Quantity: {item['quantity']}")
    else:
        print("Your cart is empty.")
    print("Total price: £{:.2f}".format(total_price))
    print("-" * 80)
    print("\n")
    print("Would you like to: ")
    print("1. See a full range of our stock")
    print("2. Add an item(s) to your cart")
    print("3. Remove item(s) from your cart")
    print("4. Checkout")
    
    choice = input("Please enter the number of the option\
 you would like to choose:\n")

    if choice == "1":
        print("Available items: ")
        print("-" * 30)
        for item in stock_list:
            print(f"Item: {item['item']:15} Price: £{item['price']:.2f}")

    elif choice == "2":
        item_name = input("What item would you like to\
 add to your cart: ").lower()
        found = False
        quantity = 0
    
        for available_item in stock_list:
            if available_item['item'].lower() == item_name:
                quantity = int(input(f"How many {available_item['item']}\
 would you like to add? "))
                if quantity <= 0:
                    print("Please enter a valid quantity.")
                    break
                
                cart_item = {
                    'item': available_item['item'],
                    'price': available_item['price'],
                    'quantity': quantity,
                }
                cart.append(cart_item)
                print(f"{quantity} {available_item['item'].capitalize()}(s)\
 have been added to your basket!")
                found = True
                break
            # 
        if not found:
            print("Sorry, that item is not available.")

    elif choice == "3":
        remove_item = input("Which item would you\
 like to remove from your cart: ").lower()
        found = False
        for cart_item in cart:
            if cart_item['item'].lower() == remove_item:
                quantity_to_remove = int(input(f"How many {cart_item['item']}\
 would you like to remove? "))
                if quantity_to_remove <= 0:
                    print("Please enter a valid quantity to remove.")
                    break
                if quantity_to_remove >= cart_item['quantity']:
                    cart.remove(cart_item)
                    print(f"All {cart_item['item'].capitalize()}(s) have\
 been removed from your basket!")
                else:
                    cart_item['quantity'] -= quantity_to_remove
                    print(f"{quantity_to_remove} {cart_item['item'].capitalize()}\
(s) have been removed from your basket!")
                found = True
                break
        if not found:
            print("Item not found in your cart!")

    elif choice == "4":
        print("Thank you for shopping at Paws N Cart")
        done = True
    else:
        print("That is not a valid option.")
