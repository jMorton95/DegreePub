from datetime import datetime
from models.ticket_model import TicketModel
from repositories.base_repository import BaseRepository
from repositories.database_connection import DatabaseConnection
from repositories.seed_database_tickets import generate_dummy_tickets

class TicketRepository(BaseRepository[TicketModel]):
    """
    TicketRepository is a class that handles database operations for the TicketModel. 
    It extends the BaseRepository class.

    Attributes
    ----------
    Inherits all attributes from the BaseRepository class.

    Methods
    -------
    __init__(db_conn: DatabaseConnection, table_name: str)
        Initializes a new instance of the TicketRepository, and seeds the database if it's empty.
    seed_database()
        Seeds the database with dummy ticket records.
    update_record(id: int, updated_record: TicketModel, date: datetime)
        Updates an existing ticket record in the database.
    log_time(id: int, remaining_time: float, logged_time: float, date: datetime) -> TicketModel
        Logs the time for a ticket and updates the remaining and logged time in the database.
    """
    
    def __init__(self, db_conn: DatabaseConnection, table_name: str):
        super().__init__(db_conn, table_name, TicketModel)

        if (self.get_count_from_table() == 0):
            print("First time run detected, beginning database seeding...")
            self.seed_database()
            print("Database seed complete!")

    def seed_database(self): 
            for record in generate_dummy_tickets():
                self.add_to_db(record)
    
    def update_record(self, id: int, updated_record: TicketModel, date: datetime):
        query = f"""
        UPDATE {self.table_name} 
        SET updated_date = ?, 
            priority = ?, 
            ticket_type = ?, 
            title = ?, 
            description = ?
        WHERE id = ?
        """

        values = (
            date,
            updated_record.priority,
            updated_record.ticket_type,
            updated_record.title,
            updated_record.description,
            id
        )

        self.db.cursor.execute(query, values)
        self.db.connection.commit()

        return self.get_by_id(id)
    

    def log_time(self, id: int, remaining_time: float, logged_time: float, date: datetime) -> TicketModel:
        query = f"""
        UPDATE {self.table_name}
        SET remaining_time = ?, logged_time = ?, updated_date = ?
        WHERE id = ?
        """

        self.db.cursor.execute(query, (remaining_time, logged_time, date, id))
        self.db.connection.commit()
        return self.get_by_id(id)




