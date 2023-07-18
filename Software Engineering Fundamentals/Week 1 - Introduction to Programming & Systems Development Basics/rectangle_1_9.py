short_side = input('Please enter the short side of your rectangle')
long_side = input('Please enter the long side of your rectangle')

if (int(short_side)):
    print('true')

print(f"The perimeter of your rectangle is: {(int(short_side) * 2) + (int(long_side) * 2)}")

print(f"The area of your rectangle is: {int(short_side) * int(long_side)}")