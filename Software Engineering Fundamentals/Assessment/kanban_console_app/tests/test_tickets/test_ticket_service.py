import unittest
from unittest.mock import Mock, patch, ANY
from models.ticket_model import TicketModel, ValidatedUserTicketInputs
from enums.ticket_type import TicketType

from services.tickets.ticket_service import TicketService


class TestTicketService(unittest.TestCase):

    def setUp(self):
        self.mock_repo = Mock()
        self.service = TicketService(self.mock_repo)

    def test_build_ticket(self):
        # Mock inputs
        inputs = ValidatedUserTicketInputs(priority=1, ticket_type=TicketType.DEPLOYMENT, title="Testing Title", description="Testing Description Longer than 25 characters", initial_estimate=10.0)
        ticket = self.service.build_ticket(inputs)
        # Test Auto generated fields are created.
        self.assertIsNotNone(ticket.created_date)
        self.assertIsNotNone(ticket.updated_date)
        self.assertEqual(ticket.title, "Testing Title")
    
    def test_create_ticket(self):
        # Create some mock user inputs & a mock ticket
        inputs = ValidatedUserTicketInputs(priority=1, ticket_type="type", title="Test", description="Desc", initial_estimate=10.0)
        mock_ticket = TicketModel(id=1, created_date=None, updated_date=None, completed=False, deleted=False, priority=1, ticket_type=TicketType.DEPLOYMENT, title="Testing Title", description="Testing Description Longer than 25 characters", initial_estimate=10.0, remaining_time=10.0, logged_time=0.0)
        #Mock the return value of adding the new ticket to the db
        self.mock_repo.add_to_db.return_value = mock_ticket
        
        #Check the return value is equal to the inputs
        result = self.service.create_ticket(inputs)
        self.assertEqual(result, mock_ticket)

    @patch('controllers.log_controller.LogController.new_log')
    def test_order_by_priority(self, mock_log):
        # Create some mock TicketModel instances...
        tickets = [
            TicketModel(id=1, priority=3, created_date=None, updated_date=None, completed=False, deleted=False, ticket_type=TicketType.DESIGN, title="Testing Title One", description="Testing Description Longer than 25 characters One", initial_estimate=10.0, remaining_time=8.0, logged_time=2.0),
            TicketModel(id=2, priority=1, created_date=None, updated_date=None, completed=False, deleted=False, ticket_type=TicketType.DEVELOPMENT, title="Testing Title Two", description="Testing Description Longer than 25 characters One", initial_estimate=5.0, remaining_time=4.0, logged_time=1.0)
        ]
        
        sorted_tickets = self.service.order_by_priority(tickets)
        
        # Assert the order based on priority or any other logic in the method
        self.assertEqual(sorted_tickets[0].priority, 1)
        self.assertEqual(sorted_tickets[1].priority, 3)

        # Assert that the logging was done correctly, e.g., we expect 3 logs: start bucket sort, finish bucket sort, and quick sort.
        self.assertEqual(mock_log.call_count, 4)

    def test_search_string_values(self):
        # Create some mock TicketModel instances
        tickets = [
            TicketModel(id=1, priority=3, created_date=None, updated_date=None, completed=False, deleted=False, ticket_type=TicketType.DESIGN, title="This is a test", description="Sample description that is very long", initial_estimate=10.0, remaining_time=8.0, logged_time=2.0),
            TicketModel(id=2, priority=1, created_date=None, updated_date=None, completed=False, deleted=False, ticket_type=TicketType.DEVELOPMENT, title="Another ticket", description="Test description that is very long", initial_estimate=5.0, remaining_time=4.0, logged_time=1.0),
            TicketModel(id=3, priority=2, created_date=None, updated_date=None, completed=False, deleted=False, ticket_type=TicketType.DEPLOYMENT, title="Third ticket", description="Another sample description that is very long", initial_estimate=7.0, remaining_time=5.0, logged_time=2.0)
        ]

        # Test for query "test"
        result = self.service.search_string_values(tickets, "test")
        self.assertEqual(len(result), 2)  # We expect two tickets to match
        self.assertEqual(result[0].id, 1)  # First matching ticket has id=1
        self.assertEqual(result[1].id, 2)  # Second matching ticket has id=2

        # Test for query "another"
        result = self.service.search_string_values(tickets, "another")
        self.assertEqual(len(result), 2)  # We expect two tickets to match
        self.assertEqual(result[0].id, 2)  # First matching ticket has id=2
        self.assertEqual(result[1].id, 3)  # Second matching ticket has id=3

        # Test for a query that doesn't match any ticket
        result = self.service.search_string_values(tickets, "nonexistent")
        self.assertEqual(len(result), 0)  # No tickets should match

    @patch('controllers.log_controller.LogController.new_log')
    def test_check_and_complete_ticket(self, mock_log):
        
        # Mock ticket with remaining_time <= 0
        completed_ticket = TicketModel(
            id=1, priority=3, created_date=None, updated_date=None, 
            completed=False, deleted=False, ticket_type=TicketType.DESIGN, 
            title="This is a test", description="Sample description Exceeding the character length", 
            initial_estimate=10.0, remaining_time=0.0, logged_time=10.0
        )

        self.service.check_and_complete_ticket(completed_ticket)

        # Ensure the `complete_record` method was called with correct parameters
        self.mock_repo.complete_record.assert_called_with(1, ANY)  # The exact datetime might vary

        # Ensure the log was generated
        mock_log.assert_called_with("Marking ticket: 1 complete. ")

        # Reset the mock after verifying with completed_ticket
        self.mock_repo.reset_mock()

        # Mock ticket with remaining_time > 0
        active_ticket = TicketModel(
            id=2, priority=1, created_date=None, updated_date=None, 
            completed=False, deleted=False, ticket_type=TicketType.DEVELOPMENT, 
            title="Another ticket", description="Test description Exceeding the character length", 
            initial_estimate=5.0, remaining_time=4.0, logged_time=1.0
        )

        self.service.check_and_complete_ticket(active_ticket)

        # Ensure the `complete_record` method was NOT called for the active ticket
        self.mock_repo.complete_record.assert_not_called()

        # Ensure no additional log was generated for the active ticket
        self.assertEqual(mock_log.call_count, 1)