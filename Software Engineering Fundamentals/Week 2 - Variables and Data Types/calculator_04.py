import operator

#Create an Object to easily map string inputs to actual operations.
OPERATORS = {
    'add': operator.add,
    'sub': operator.sub,
    'mult': operator.mul,
    'div': operator.truediv,
    'sq': operator.mul,
    'pow': operator.pow
}

num_one = float(input("Enter number 1 "))
num_two = float(input("Enter number 2 "))

chosen_operator = input(f"Please enter one of the following operators: {', '.join(OPERATORS)} ")

while (chosen_operator not in OPERATORS):
    chosen_operator = input(f"That was an invalid operator, please enter one of the following: {', '.join(OPERATORS)} ")

#The only time I'd need an IF statement for this is because every other calculation other than 'square' expects 2 arguments.
if (chosen_operator == 'sq'):
    for num in [num_one, num_two]:
        print(OPERATORS[chosen_operator](num, 2))
else:
    print(OPERATORS[chosen_operator](num_one, num_two))
