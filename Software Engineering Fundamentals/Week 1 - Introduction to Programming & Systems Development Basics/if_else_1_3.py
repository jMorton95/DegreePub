from simple_sequence_1_1 import get_card_value_from_user

#NOTE: This exercise would be trivialised with the 'Operators' interface 
VALID_OPERATORS = ('+', '*')

def get_operator_from_user(operators: tuple) -> str:
    formatted_operators = ''.join(f"'{value}' " for value in operators)
    user_input = input(f"Please input one of the following operators: {(formatted_operators)}")

    '''NOTE: I tried to use operators.__contains__(user_input) first, from JS/C# familiarity.
    However apparently 'in' calls this under the hood anyway.'''
    while True:
        if (user_input in operators):
            return user_input
        else:
            user_input = input(f"The operator you selected was invalid, please choose from: {(formatted_operators)}")

def calculate_from_input(first_number: int, second_number: int, operator: str) -> int:
    if (operator == VALID_OPERATORS[0]):
        return first_number + second_number
    elif (operator == VALID_OPERATORS[1]):
        return first_number * second_number
    else:
        print("Error occurred")

def main():
    card_one = get_card_value_from_user("Card One")
    card_two = get_card_value_from_user("Card Two")
    chosen_operator = get_operator_from_user(VALID_OPERATORS)
    print(calculate_from_input(card_one, card_two, chosen_operator))

#Ensure this only runs if this script is being executed directly
if __name__ == '__main__':
    main()