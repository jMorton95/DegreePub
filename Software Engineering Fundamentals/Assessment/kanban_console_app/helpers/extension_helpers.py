import re

def convert_float_to_time(time_float):
    hours = int(time_float)
    minutes = (time_float - hours) * 60
    return hours, round(minutes)


def validate_as_int(input: str):
    try:
        int(input)
        return True
    except ValueError:
        return False
    
def validate_as_float(input: str):
    try:
        float(input)
        return True
    except ValueError:
        return False
    
def find_option_by_number(options: list[str], user_input: int):
    for opt in options:
        # Extract the number from the beginning of the string
        match = re.match(r'^(\d+):', opt)
        if match and int(match.group(1)) == user_input:
            return opt
    return "Unknown Option"

def check_option_in_range(options: int | float, opt: int | float):
    return True if opt <= options and opt > 0 else False