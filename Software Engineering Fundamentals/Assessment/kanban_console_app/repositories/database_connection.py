import sqlite3
from environment.env import DB_CONNECTION

class DatabaseConnection:
    """
    Database Instance that will be passed to our Application

    Methods
    -------

    close(self)
        Closes the database connection.
    """
    def __init__(self):
        self.connection = sqlite3.connect(DB_CONNECTION)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

