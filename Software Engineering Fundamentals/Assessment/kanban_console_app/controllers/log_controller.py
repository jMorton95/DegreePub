from datetime import datetime
from environment.env import LOG_FILE_NAME


class LogController:
    """ 
    A controller class for handling operations related to logs. 
    It provides methods to create a new log file, count lines in the log file, 
    add a new log and read all logs.

    Attributes:
        LOG_FILE_NAME: Default log file name. Needs to be defined elsewhere in the code.
    """

    def __create_log_file(file_name: str = LOG_FILE_NAME):
        """
        Creates a new log file.

        Args:
            file_name (str): The name of the file to create. Defaults to LOG_FILE_NAME.

        Returns:
            None
        """
        with open(file_name, 'x') as file:
            file.write(f"1: Log File created at: {datetime.now()}")

    def __get_line_count(file_name: str = LOG_FILE_NAME):
        """
        Gets the line count of the log file. If the file doesn't exist, creates a new one.

        Args:
            file_name (str): The name of the file to get line count. Defaults to LOG_FILE_NAME.

        Returns:
            int: The number of lines in the log file.
        """
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
            return len(lines) + 1
        except FileNotFoundError:
            LogController.__create_log_file(file_name)
            return LogController.__get_line_count(file_name)

    @staticmethod
    def new_log(msg: str, file_name: str = LOG_FILE_NAME):
        """
        Writes a new log entry to the log file.

        Args:
            msg (str): The message to be logged.
            file_name (str): The log file where the message will be logged. Defaults to LOG_FILE_NAME.

        Returns:
            None
        """
        line_number = LogController.__get_line_count(file_name)
        with open(file_name, 'a') as file:
            file.write(f"\n{line_number}: {msg} - at {datetime.now()}")

    @staticmethod
    def read_logs():
        """
        Reads all logs and prints the count of lines that contain the word "User".

        Returns:
            None
        """
        with open(LOG_FILE_NAME, 'r') as file:
            lines = file.readlines()
            print(len([l for l in lines if "User" in l]))
