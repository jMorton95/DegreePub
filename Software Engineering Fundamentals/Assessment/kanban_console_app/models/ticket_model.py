from dataclasses import dataclass
from controllers.log_controller import LogController
from models.base_model import BaseModel
from enums.ticket_type import TicketType
"""
This module contains our main dataclass for Object Relational Mapping
"""


@dataclass
class ValidatedUserTicketInputs():
    priority: int
    ticket_type: TicketType
    title: str
    description: str
    initial_estimate: float

    """
    A dataclass representing the user input driven content of the Ticket model.
    It contains the following properties:
    - ticket_type: a TicketType enumeration value
    - name: a string representing the ticket name
    - description: a string describing the ticket
    - initial_estimate: a float representing the initial time estimate for the ticket
    - remaining_time: a float representing the remaining time to complete the ticket
    - logged_time: a float representing the time already spent on the ticket
    - priority: an integer between 1 and 5
    """


@dataclass
class TicketModel(ValidatedUserTicketInputs, BaseModel):
   # Combines BaseModel properties that all Models inherit with User Input fields from ValidatedUserTicketInputs and stores auto-calculated properties.
    remaining_time: float
    logged_time: float

    def __post_init__(self):
        # Currently disabled, but was used during Development for tracking Object creation order & garbage collection
        # LogController.new_log(f"Created Object in Memory: {hex(id(self))} - TicketID - {self.id} - TicketName - {self.title}", "memory.txt")
        return super().__post_init__()

    # def __del__(self):
        # LogController.new_log(f"Garbage Collecting: {hex(id(self))} - TicketID - {self.id} - TicketName - {self.title}", "memory.txt")


@dataclass
class ValidUpdateFields():
    """
    A dataclass representing the valid fields that can be updated for a ticket.

    Attributes:
        priority (int): The priority level of the ticket.
        ticket_type (TicketType): The type of the ticket.
        title (str): The title of the ticket.
        description (str): The description of the ticket.
    """
    
    priority: int
    ticket_type: TicketType
    title: str
    description: str
