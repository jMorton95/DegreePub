from datetime import datetime

class Formatter():
    """
    Formatter is a utility class for formatting various types of data into a more human-readable format.

    Methods
    -------
    make_readable(key: str) -> str
        Transforms a snake_case string into a properly spaced and capitalized string.
    day_suffix(day: int)
        Returns the correct ordinal suffix for a day of the month.
    format_date(date: datetime)
        Formats a datetime object into a readable string with the correct day suffix.
    format_object(obj) -> str
        Takes an object and formats each of its properties into a list of readable strings.
    """
     
    def make_readable(self, key: str) -> str:
        return ' '.join(map(str.capitalize, key.split('_')))
    
    def day_suffix(self, day: int):
        return ("th" if 4 <= day <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th"))

    def format_date(self, date: datetime):
        return date.strftime(f"%H:%M %p %d{self.day_suffix(date.day)} %B %y")
    
    def format_object(self, obj) -> str:
        formatted_entries = []
        for (key, value) in vars(obj).items():
            if isinstance(value, datetime):
                formatted_value = self.format_date(value)
            else:
                formatted_value = str(value)
            formatted_entries.append(f"{self.make_readable(key)}: {formatted_value}  ")
        formatted_entries.append(" ")
        return formatted_entries