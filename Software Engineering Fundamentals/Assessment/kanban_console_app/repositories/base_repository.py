from dataclasses import fields
from datetime import datetime
from enum import Enum, EnumMeta
from typing import List, Optional
from models.base_model import BaseModel
from repositories.database_connection import DatabaseConnection
from typing import Type, TypeVar, Generic

T = TypeVar('T', bound=BaseModel)

class BaseRepository(Generic[T]):
    type_map = {
        int: "INTEGER",
        Optional[int]: "INTEGER PRIMARY KEY",
        float: "REAL",
        bool: "BOOLEAN",
        str: "TEXT",
        datetime: "TEXT"
    }

    def __init__(self, db_connection: DatabaseConnection, table_name: str, model_class: Type[T]):
        self.db = db_connection
        self.table_name = table_name
        self.model_class = model_class
        self.create_table(self.model_class)

    
    
    def create_table(self, model: T):
        column_definitions = []
        #Map generic fields to a predefined SQL Type
        for field in fields(model):
            sql_type = self.type_map.get(field.type)
            
            #Fringe condition for Enums.
            if isinstance(field.type, EnumMeta):
                sql_type = "TEXT"

            if not sql_type:
                raise ValueError(f"Unsupported field type: {field.type} for field {field.name}")

            column_definitions.append(f"{field.name} {sql_type}")

        self.db.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                {', '.join(column_definitions)}
            )
        ''')
        self.db.connection.commit()

    def add_to_db(self, item: T) -> T:
        """
        Adds a new item to the database.

        Args:
            item (T): The item object to be added.

        Returns:
            T: The newly created item object.
        """

        # Prepare our column names, exclude ID.
        column_names = [f.name for f in fields(item) if f.name != 'id']

        # Prepare the query string
        query = f"""
        INSERT INTO {self.table_name} ({', '.join(column_names)})
        VALUES ({', '.join('?' for _ in column_names)})
        """

        values = []
        #Use of Enums require us to test each property before returning the value.
        for column in column_names:
            value = getattr(item, column) 
            if isinstance(value, Enum):
                value = str(value.value)
            values.append(value)

        self.db.cursor.execute(query, values)
        self.db.connection.commit()

        return self.get_by_id(self.db.cursor.lastrowid)

    def get_by_id(self, id: int) -> T:
        self.db.cursor.execute(f'SELECT * FROM {self.table_name} WHERE id = ?', (id,))
        result = self.db.cursor.fetchone()
        return self.model_class(*result) if result else None
    
    def get_all(self) -> List[T]:
        self.db.cursor.execute(f'SELECT * FROM {self.table_name}')
        return [self.model_class(*row) for row in self.db.cursor.fetchall()]
    
    def get_count_from_table(self):
        self.db.cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        return self.db.cursor.fetchone()[0]
    
    def delete_record(self, id: int, date: datetime) -> T:
        query = f"""
        UPDATE {self.table_name}
        SET deleted = ?, updated_date = ?
        WHERE id = ?
        """

        self.db.cursor.execute(query, (1, date, id))
        self.db.connection.commit()
        return self.get_by_id(id)
    
    def complete_record(self, id: int, date: datetime) -> T:
        query = f"""
        UPDATE {self.table_name}
        SET completed = ?, updated_date = ?
        WHERE id = ?
        """

        self.db.cursor.execute(query, (1, date, id))
        self.db.connection.commit()
        return self.get_by_id(id)
    
                

