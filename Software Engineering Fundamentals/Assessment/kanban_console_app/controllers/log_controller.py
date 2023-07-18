from datetime import datetime
from environment.env import LOG_FILE_NAME

class LogController:

    def __create_log_file(file_name: str = LOG_FILE_NAME):
        with open(file_name, 'x') as file:
            file.write(f"1: Log File created at: {datetime.now()}")

    def __get_line_count(file_name: str = LOG_FILE_NAME):
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
            return len(lines) + 1
        except FileNotFoundError:
            LogController.__create_log_file(file_name)
            return LogController.__get_line_count(file_name)

    @staticmethod
    def new_log(msg: str, file_name: str = LOG_FILE_NAME):
        line_number = LogController.__get_line_count(file_name)
        with open(file_name, 'a') as file:
            file.write(f"\n{line_number}: {msg} - at {datetime.now()}")
            
    @staticmethod
    def read_logs():
        with open(LOG_FILE_NAME, 'r') as file:
            lines = file.readlines()
            print(len([l for l in lines if "User" in l]))
       

        