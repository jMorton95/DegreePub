def main():
    # Input the value of two cards
    card1 = int(input("Enter the value of the first card: "))
    card2 = int(input("Enter the value of the second card: "))

    # If the value of the second card is greater than 5, add its value to the value of the first card
    if card2 > 5:
        card1 += card2

    # Output the value of the first card
    print("Value of the first card:", card1)

if __name__ == "__main__":
    main()