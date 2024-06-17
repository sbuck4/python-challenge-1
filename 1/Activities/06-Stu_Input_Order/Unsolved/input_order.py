# Take input of an item the user wants to purchase
purchase_item = input("What Item would you like to buy")

# Ask how much the item costs and cast it as a number.
# What type of number should it be cast as?
cost = float(input("How much does this item cost"))

# Ask what quantity of the item should be purchased and cast it as a number.
# What type of number should it be cast as?
quantity = int(input("How many would you like to buy?"))

# Print the item cost along with its data type
print("The total cost is", quantity*cost)

# Print the item quantity along with its data type
print(type(quantity))

# Print results
print(purchase_item, "$", cost*quantity)