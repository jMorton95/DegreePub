from helpers.extension_helpers import check_option_in_range, find_option_by_number, validate_as_float, validate_as_int
from helpers.print_colours import print_green, print_red, prompt_underline


class PromptManager:
    """
    PromptManager class is responsible for managing user inputs from the terminal. It provides various functions to take user input and perform validation checks.

    Methods
    -------
    get_user_choice(options)
        Prompts the user to make a choice from a list of options and returns the chosen option.
    get_number_from_user(as_float: bool)
        Prompts the user to enter a number, validates the input, and returns the number as a float if 'as_float' is true, or as an int otherwise.
    get_number_from_user_in_range(top_end: int | float)
        Prompts the user to enter a number within a specified range and returns the number.
    get_raw_string_from_user() -> str
        Prompts the user to enter a string and returns the input string.
    get_user_confirmation(opt_string: str, id: int = 0) -> bool
        Prompts the user for a Yes or No confirmation and returns True if 'Yes', or False otherwise.
    continue_message()
        Displays a message prompting the user to press any key to continue.
    """
    
    def get_user_choice(self, options: list[str]) -> int | float:
        choice = self.get_number_from_user_in_range(len(options))
        print_green(f"\n{find_option_by_number(options, choice)}\n")

        return choice
        
    def get_number_from_user(self, as_float: bool) -> int | float:
        while True: 
            user_input = prompt_underline("\nPlease enter your choice (Number): ")
            
            if (not as_float and validate_as_int(user_input) == False):
                print_red(f"\n'{user_input}' is not a number.")
                continue
            elif (as_float and validate_as_float(user_input) == False):
                print_red(f"\n'{user_input}' is not a number.")
                continue
        
            return int(user_input) if not as_float else float(user_input)
        
    def get_number_from_user_in_range(self, top_end: int | float) -> int | float:
        while True: 
            choice = self.get_number_from_user(as_float = True if isinstance(top_end, float) else False)
            
            if (check_option_in_range(top_end, choice) == False):
                print_red(f"\n{choice} was not within range 1 to {top_end}. ")
                continue

            return choice
        
    def get_raw_string_from_user(self) -> str: 
        return prompt_underline("\nPlease enter your search query: ")
    
    def get_user_confirmation(self, opt_string: str, id: int = 0) -> bool:
        while True:
            print_green(f"Do you want to {opt_string}{id if id > 0 else ''}?\n")
            response = prompt_underline(f"Enter Y for Yes or N for No: ").strip()
            if response.lower() in ['y', 'n']:
                return response.lower() == 'y'
            else:
                print_red("\nInvalid input, please enter Y or N.")

    def continue_message(self):
        prompt_underline("\nPress any key to continue.\n ")

    