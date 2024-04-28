from dataclasses import dataclass
from typing import Optional

@dataclass
class TicketPreviewModel():
    """
    A data model for representing a preview of a ticket in a ticketing system.

    Attributes
    ----------
    id : int, optional
        The unique identifier of the ticket, by default None
    priority : int
        The priority level of the ticket, where a lower value indicates a more urgent ticket
    title : str
        The title or brief description of the ticket
    remaining_time : float
        The estimated remaining time to resolve the ticket. 
    """
    id: Optional[int]
    priority: int
    title: str
    remaining_time: float
    