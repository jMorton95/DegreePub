from datetime import datetime
from models.ticket_model import TicketModel
from repositories.base_repository import BaseRepository
from repositories.database_connection import DatabaseConnection
from repositories.seed_database_tickets import generate_dummy_tickets

class TicketRepository(BaseRepository[TicketModel]):
    def __init__(self, db_conn: DatabaseConnection, table_name: str):
        super().__init__(db_conn, table_name, TicketModel)

        if (self.get_count_from_table() == 0):
            self.seed_database()

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




