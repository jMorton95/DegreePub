from environment.env import DB_TICKET_STRING

from controllers.ticket_controller import TicketController
from repositories.database_connection import DatabaseConnection
from repositories.ticket_repository import TicketRepository

from services.terminal.formatter import Formatter
from services.terminal.output_manager import OutputManager, PromptManager
from services.tickets.ticket_input_validation_service import TicketInputValidationService
from services.tickets.ticket_service import TicketService

# This metaclass ensures a single instance of a class is created and shared.
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# This class uses Singleton metaclass to create a single instance
# It creates instances of DatabaseConnection and OutputManager
class Configuration(metaclass=Singleton):
    def __init__(self):
        # Create a DatabaseConnection instance if not exists
        if not hasattr(self, 'app_db_conn'):
            self.app_db_conn = DatabaseConnection()

        # Create an OutputManager instance with Formatter and PromptManager if not exists
        if not hasattr(self, 'output_manager'):
            self.output_manager = OutputManager(
                Formatter(),
                PromptManager(),
            )

# TicketConfiguration inherits from Configuration class and additionally composes the TicketController.
class TicketConfiguration(Configuration):
    def __init__(self):
        super().__init__()
        
    # This method composes the TicketController with necessary dependencies
    def compose_ticket_controller(self) -> TicketController:
        return TicketController(
            TicketService(
                TicketRepository(
                    self.app_db_conn,
                    DB_TICKET_STRING,
                )
            ),
            TicketInputValidationService(),
            self.output_manager,
        )
        
