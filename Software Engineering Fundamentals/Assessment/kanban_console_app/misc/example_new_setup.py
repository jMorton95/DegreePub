from dataclasses import dataclass
from datetime import datetime
from models.base_model import BaseModel
from repositories.base_repository import BaseRepository
from repositories.database_connection import DatabaseConnection
from services.base_service import BaseService

#NOTE: Not intended to actually be run. Bootstrapped setup to demonstrate creating a new application.
def main():
        #Define a new dataclass with any desired properties.
        @dataclass
        class ExampleNewModel(BaseModel):
            example_new_int: int
            example_new_string: str
            example_new_date: datetime
            example_new_bool: bool

        #Define a new Repository, passing the desired Model.
        class ExampleNewRepository(BaseRepository[ExampleNewModel]):
            def __init__(self, db_conn: DatabaseConnection, table_name: str):
                super().__init__(db_conn, table_name, ExampleNewModel)

        #Define a new Service, passing the desired Model.
        class ExampleNewService(BaseService[ExampleNewModel]):
            def __init__(self, example_new_repository: ExampleNewRepository):
                super().__init__(example_new_repository)
                self.example_new_repository = example_new_repository


        #Instantiate, triggering creation of new table.
        new_service = ExampleNewService(
                        ExampleNewRepository(
                            DatabaseConnection(), "Example_New_Table"
                        )
                    )
        

        new_service.get_all() #Generic Implementation