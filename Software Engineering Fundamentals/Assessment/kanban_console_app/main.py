from config.composition_manager import TicketConfiguration
from controllers.log_controller import LogController



def main():
    app = TicketConfiguration().compose_ticket_controller()
    app.start()

   
if __name__ == "__main__":
    main()
