DISCOUNT = 0.90
VAT = 1.2
DELIVERY = 4.5

price_before_calculation = float(input("Please input your price"))

calculated_price = ((price_before_calculation * DISCOUNT) * VAT) + DELIVERY

print(f"Your total is: {calculated_price}")
