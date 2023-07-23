from dataclasses import fields
from controllers.log_controller import LogController
from helpers.print_colours import print_green, print_red
from services.tickets.ticket_input_validation_service import TicketInputValidationService
from services.terminal.output_manager import OutputManager
from services.tickets.ticket_service import TicketService


class TicketController():
    """
    Controller class for handling ticket-related operations.

    Attributes:
        service (TicketService): Service for handling ticket-related business logic.
        input_validator (TicketInputValidationService): Service for validating user input related to tickets.
        output_manager (OutputManager): Service for managing output to the terminal.
        commands (dict): Mapping of user commands to corresponding methods.
    """

    def __init__(self, ticket_service: TicketService, ticket_input_validator: TicketInputValidationService, output_manager: OutputManager):
        """
        Initialize a new instance of the TicketController class.

        Args:
            ticket_service (TicketService): The ticket service.
            ticket_input_validator (TicketInputValidationService): The ticket input validator.
            output_manager (OutputManager): The output manager.
        """
        self.service = ticket_service
        self.input_validator = ticket_input_validator
        self.output_manager = output_manager
        self.commands = {
            1: self.preview_all,
            2: self.view_by_id,
            3: self.new_ticket,
            4: self.update_ticket,
            5: self.delete_ticket,
            6: self.search_by_name,
            7: self.show_completed,
            8: self.show_deleted,
            9: self.show_all_raw,
            0: self.quit
        }

    def start(self):
        """
        Start the ticket controller, logging the start and end of the application session.
        Handles command execution and continues until the quit command is given.
        """
        LogController.new_log("Application Started")

        run = True
        while run:
            
            user_command = self.output_manager.startup_message()
            LogController.new_log(f"User attempted: {str(self.commands[user_command].__name__)}")
            run = self.commands[user_command]()

            if run:
                self.output_manager.prompt_manager.continue_message()
            if not run:
                LogController.new_log("Successfully Quit Application")

    def preview_all(self):
        """
        Preview all non-deleted, non-completed tickets in order of priority.
        """

        non_deleted_or_completed = self.service.filter_complete(False, self.service.filter_deleted(False, self.service.get_all()))

        ordered_tickets = self.service.order_by_priority(non_deleted_or_completed)

        print_green(f"There are {len(ordered_tickets)} outstanding tickets, and {len(non_deleted_or_completed)} in total!\n")

        preview = self.service.create_preview(ordered_tickets)
        self.output_manager.single_line(preview)
        LogController.new_log(f"Preview All Succeeded. ")
        return True

    def view_by_id(self):
        """
        View a ticket by its ID, and optionally log time to it if it's not completed.
        """

        id = self.output_manager.get_id_input(self.service.get_count())
        ticket = self.service.get_by_id(id)

        if (self.service.check_if_deleted(ticket)):
            self.output_manager.no_records_found(f"Record deleted. {ticket.updated_date}")

            LogController.new_log(f"User searched for deleted record: {ticket.id}: {ticket.title}")
            return True

        self.output_manager.multi_line(ticket)

        if (self.service.check_if_completed(ticket)):
            LogController.new_log(f"Record: {ticket.id} - {ticket.title} is complete. Not prompting user to log time")
            return True

        if self.output_manager.prompt_manager.get_user_confirmation("log time to ticket: ", id):
            
            LogController.new_log(f"User logging time to {ticket.id}: {ticket.title}. ")
            time_to_log = self.output_manager.display_time_logging_information(ticket.remaining_time)

            LogController.new_log(f"Attempting to log {time_to_log} to {ticket.id}: {ticket.title}")
            updated_ticket = self.service.log_time(ticket, time_to_log)

            LogController.new_log(f"Successfully logged time. Total time logged: {updated_ticket.logged_time}. Remaining time: {updated_ticket.remaining_time}")
            self.output_manager.show_time_logged(updated_ticket.logged_time, updated_ticket.remaining_time)

        return True

    def new_ticket(self):
        """
        Create a new ticket based on user input.
        """
        
        input_props = self.input_validator.generate_validated_user_ticket_inputs()
        LogController.new_log(f"Attempting to create new ticket from inputs: {' '.join(f'{input.name}: {getattr(input_props, input.name)}' for input in fields(input_props))}")

        ticket = self.service.create_ticket(input_props)
        LogController.new_log(f"Successfully created new ticket - {ticket.id}: {ticket.title}")

        self.output_manager.single_line(ticket)
        return True

    def update_ticket(self):
        """
        Update a selected ticket based on user input. If the ticket is deleted, no update is performed.
        """

        selected_ticket = self.service.get_by_id(
            self.output_manager.get_id_input(self.service.get_count()))

        if (self.service.check_if_deleted(selected_ticket)):
            LogController.new_log( f"Updating record {selected_ticket.id}: {selected_ticket.title} failed. Deleted.")
            self.output_manager.no_records_found(f"Record deleted. {selected_ticket.updated_date}")
        else:
            field_to_update = self.output_manager.display_update_information(self.service.populate_update_fields(selected_ticket))
            updated_value = self.input_validator.call_chosen_update_function(field_to_update)
            self.service.update_record(selected_ticket, field_to_update, updated_value)
            print_green(f"Successfully updated record {selected_ticket.id} : {selected_ticket.title}.")
            LogController.new_log(f"Successfully updated record {selected_ticket.id} : {selected_ticket.title}.")
        return True

    def delete_ticket(self):
        """
        Delete a ticket based on user input. If the ticket is already deleted, no action is performed.
        """
         
        id = self.output_manager.get_id_input(self.service.get_count())
        record = self.service.get_by_id(id)
        if (record.deleted):
            print_red("Record already deleted. ")
            LogController.new_log(f"Deleting record {record.id}: {record.title} failed. Already deleted.")
            return

        self.output_manager.single_line(record)

        if (self.output_manager.prompt_manager.get_user_confirmation("delete record ", id)):
            LogController.new_log(f"Deleted record {record.id}: {record.title} successfully.")
            self.output_manager.multi_line(self.service.delete_record(id))

        return True

    def search_by_name(self):
        """
        Search for tickets by a string query input by the user.
        """
        tickets = self.service.get_all()
        query = self.output_manager.prompt_manager.get_raw_string_from_user()
        LogController.new_log(f"User searched for: {query}")

        filtered = self.service.search_string_values(tickets, query)
        LogController.new_log(f"Found: {len(filtered)} records.")

        self.output_manager.multi_line(filtered)
        return True

    def show_completed(self):
        """
        Show all non-deleted, completed tickets.
        """

        non_deleted = self.service.filter_deleted(False, self.service.get_all())
        completed = self.service.filter_complete(True, non_deleted)

        LogController.new_log(f"Found: {len(completed)} completed records.")
        self.output_manager.single_line(completed)
        return True

    def show_deleted(self):
        """
        Show all deleted tickets.
        """

        deleted = self.service.filter_deleted(True, self.service.get_all())
        LogController.new_log(f"Found: {len(deleted)} deleted records.")
        self.output_manager.single_line(deleted)
        return True

    def show_all_raw(self):
        """
        Show all tickets in raw form.
        """

        self.output_manager.multi_line(self.service.get_all())
        return True

    def quit(self):
        """
        Quit the application. Before quitting, the user is asked for confirmation.
        """
        
        self.service.ticket_repository.db.close()
        return not self.output_manager.prompt_manager.get_user_confirmation("quit the application")
