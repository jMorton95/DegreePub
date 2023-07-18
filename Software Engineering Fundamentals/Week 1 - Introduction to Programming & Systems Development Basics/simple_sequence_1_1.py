def get_card_value_from_user(card_name) -> int:
 
    while True:
        input_str = input(f"Please enter the number of: {card_name}")

        try:
            user_input = int(input_str)
            return user_input
        except ValueError:
            print("That's not a valid number, please enter a number.")

def sum_of_integers(first_number: int, second_number: int, *numbers: int) -> int:
    """
    Sums any number of parameters and returns the result

    Args: 
        first_number (int): Required integer
        second_number (int): Required integer
        *numbers (int): Optional additional integers

    Returns: 
        int: The sum of all our arguments
    """

    #Typically we would want to Type Check our *numbers arguments as int
    # We'll skip it for the exercise purposes.
    # (Validating user input ahead of time)

    accumulator = first_number + second_number

    for number in numbers:
        accumulator += number

    return accumulator

def main():
    first_card = get_card_value_from_user("Card One")
    second_card = get_card_value_from_user("Card Two")

    total_of_cards = sum_of_integers(first_card, second_card)

    print(f"The sum of these numbers is: {total_of_cards}")

#Ensure this only runs if this script is being executed directly
if __name__ == '__main__':
    main()
