from simple_sequence_1_1 import get_card_value_from_user, sum_of_integers

def add_numbers_if_above_minimum(first_number: int, second_number: int, minimum_for_addition) -> tuple[int, bool]:
    """
    Adds two numbers if the second number is greater than a minimum value.

    Args:
        first_number (int): The first number to add.
        second_number (int): The second number to add.
        minimum_for_addition (int): The minimum value for the second number to trigger addition.

    Returns:
        tuple: A tuple containing the sum of the two numbers and a boolean value indicating whether
        the second number was greater than the minimum value (True) or not (False).
    """
     
    if (second_number > minimum_for_addition):
        return (first_number + second_number, True)
    else:
        return (first_number, False)

def main():
    card_one = get_card_value_from_user("Card One")
    card_two = get_card_value_from_user("Card Two")

    result, condition_result = add_numbers_if_above_minimum(card_one, card_two, 5)
    
    print(f"The result was {result}, the condition evaluated to {condition_result}")

#Ensure this only runs if this script is being executed directly
if __name__ == '__main__':
    main()
