print("Welcome to the Skibidi Shop!")

item = input("Which item would you like to buy?: ")
price = float(input("How much does it cost?: "))
amount = int(input(f"How much of {item} do you want?: "))

end_price = price * amount


print(f"You have put now in your cart {amount}x {item}")
print(f"Your price will be {end_price}€")
print("Thank you for shopping with us!")



