price_per_bag = int(input("What is the price of a bag of sweets? (In pennies)"))
total_pennies = int(input("How many pennies do you have?"))

bags_bought = total_pennies // price_per_bag
remainder = total_pennies - (price_per_bag * bags_bought)

print(f"You bought: {bags_bought} bags and have {remainder} pennies left")