item_in_store = {"shawarma": 4.99,
                  "chicken": 8.99,
                  "salad": 3.99,
                  "sauce": 1.4}


print("Welcome to the Skibidi Shop!")

item = input("Which item would you like to buy?: ").lower()
if item in item_in_store:
    price = item_in_store.get(item)
    amount = int(input(f"How much of {item.capitalize()} do you want?: "))

    end_price = price * amount

    print(f"You have put now in your cart {amount}x {item.capitalize()}")
    print(f"Your price will be {end_price:.2f}€")
    print("Thank you for shopping with us!")
else:
    print(f"We do not have {item.capitalize()} please choose our items in store.")



