price_of_item = float(input("Please input the price of the item"))

#Single line ternary style. Unreadable.
discounted_price_ternary = price_of_item * 0.6 if price_of_item >= 400 else price_of_item * 0.8 if price_of_item >= 200 and price_of_item <= 399 else price_of_item * 0.9 if price_of_item >= 100 and price_of_item <= 199 else price_of_item if price_of_item > -1 else "Error, price per item is negative"

print(f"Cheaty Ternary: {discounted_price_ternary}")

#Proper solution using an Obj to store our discount brackets * percentages

def get_discounted_price(price_of_item):

    """Iterable Obj to contain the thresholds & discounts.
        I actually had to do something very similar for a client in JavaScript recently, with the prices coming from a DB and there being many of them.
        The discount thresholds & percentage came from a separate table so it was easy to extend with a descending sorted Array of discounts. 
    """
    discounts = {
        400: 0.6,
        200: 0.8,
        100: 0.9,
        0: 1
    }

    if (price_of_item < 0):
        return "Error, price below zero"

    #"For [Key, Value]:"
    for limit, discount in discounts.items():
        if price_of_item >= limit:
            return price_of_item * discount
        
discounted_price = get_discounted_price(price_of_item)
print(f"Extendable solution: {discounted_price}")