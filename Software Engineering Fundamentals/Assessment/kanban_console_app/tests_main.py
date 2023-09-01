import unittest
from tests.test_helpers.test_extension_helpers import TestExtensionHelpers
from tests.test_helpers.test_print_colours import TestPrintColours
from tests.test_tickets.test_ticket_input_validation_service import TestTicketInputValidationService
from tests.test_tickets.test_ticket_service import TestTicketService

def suite(): 
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestExtensionHelpers))
    suite.addTest(unittest.makeSuite(TestPrintColours))
    suite.addTest(unittest.makeSuite(TestTicketInputValidationService))
    suite.addTest(unittest.makeSuite(TestTicketService))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=5, descriptions=True).run(suite())
   