import math

a = float(input("What is the length of your short side?"))
b = float(input("What is the length of your second shortest side?"))

c = round(math.sqrt(a ** 2 + b ** 2), 2)

print(f"Length of long side is: {c}")