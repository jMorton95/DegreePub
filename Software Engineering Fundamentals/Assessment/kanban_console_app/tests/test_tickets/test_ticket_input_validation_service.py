import unittest
from unittest.mock import patch, Mock
from enums.ticket_type import TicketType
from services.tickets.ticket_input_validation_service import TicketInputValidationService

class TestTicketInputValidationService(unittest.TestCase):

    def setUp(self):
        self.service = TicketInputValidationService()

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', return_value="3")
    def test_prompt_and_validate_priority_valid(self, _):
        result = self.service.prompt_and_validate_priority()
        self.assertEqual(result, 3)

    @patch('services.tickets.ticket_input_validation_service.print_red')
    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["8", "2"])
    def test_prompt_and_validate_priority_invalid_then_valid(self, mock_input, mock_print):
        result = self.service.prompt_and_validate_priority()
        mock_print.assert_called_once()
        self.assertEqual(result, 2)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["7", "-1", "0", "3"])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_and_validate_priority_multiple_invalid(self, mock_print, mock_input):
        result = self.service.prompt_and_validate_priority()
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(result, 3)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["test", "3"])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_and_validate_priority_non_numeric(self, mock_print, mock_input):
        result = self.service.prompt_and_validate_priority()
        mock_print.assert_called_once()
        self.assertEqual(result, 3)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["EXIT"])
    def test_prompt_and_validate_priority_exit(self, mock_input):
        result = self.service.prompt_and_validate_priority()
        self.assertIsNone(result)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["1"])
    def test_prompt_and_validate_priority_min_boundary(self, mock_input):
        result = self.service.prompt_and_validate_priority()
        self.assertEqual(result, 1)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["5"])
    def test_prompt_and_validate_priority_max_boundary(self, mock_input):
        result = self.service.prompt_and_validate_priority()
        self.assertEqual(result, 5)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["eXiT"])
    def test_prompt_and_validate_priority_case_insensitive_exit(self, mock_input):
        result = self.service.prompt_and_validate_priority()
        self.assertIsNone(result)


    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["DEVELOPMENT"])
    def test_valid_ticket_type(self, mock_input):
        result = self.service.prompt_and_validate_ticket_type()
        self.assertEqual(result, TicketType.DEVELOPMENT)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["INVALID", "TESTING"])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_invalid_then_valid_ticket_type(self, mock_print, mock_input):
        result = self.service.prompt_and_validate_ticket_type()
        mock_print.assert_called_once()
        self.assertEqual(result, TicketType.TESTING)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["NON_EXISTENT"])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_non_existent_ticket_type(self, mock_print, mock_input):
        with self.assertRaises(StopIteration):
            self.service.prompt_and_validate_ticket_type()
        mock_print.assert_called_once()
   

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["development"])
    def test_case_insensitive_ticket_type(self, mock_input):
        result = self.service.prompt_and_validate_ticket_type()
        self.assertEqual(result, TicketType.DEVELOPMENT)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["INVALID1", "INVALID2", "DEPLOYMENT"])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_multiple_invalid_then_valid_ticket_type(self, mock_print, mock_input):
        result = self.service.prompt_and_validate_ticket_type()
        self.assertEqual(mock_print.call_count, 2)
        self.assertEqual(result, TicketType.DEPLOYMENT)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["PLANNING", "DESIGN", "DEVELOPMENT", "TESTING", "DEPLOYMENT", "DOCUMENTATION", "SUPPORT"])
    def test_all_valid_ticket_types(self, mock_input):
        for t_type in TicketType:
            result = self.service.prompt_and_validate_ticket_type()
            self.assertEqual(result, t_type)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["DeVelOPmEnt"])
    def test_mixed_case_valid_ticket_type(self, mock_input):
        result = self.service.prompt_and_validate_ticket_type()
        self.assertEqual(result, TicketType.DEVELOPMENT)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["", "TESTING"])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_empty_input_then_valid(self, mock_print, mock_input):
        result = self.service.prompt_and_validate_ticket_type()
        mock_print.assert_called_once()
        self.assertEqual(result, TicketType.TESTING)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["  TESTING  "])
    def test_ticket_type_with_whitespaces(self, mock_input):
        result = self.service.prompt_and_validate_ticket_type()
        self.assertEqual(result, TicketType.TESTING)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=["123DEVELOPMENT!", "DEVELOPMENT"])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_ticket_type_with_numbers_special_chars(self, mock_print, mock_input):
        result = self.service.prompt_and_validate_ticket_type()
        mock_print.assert_called_once()
        self.assertEqual(result, TicketType.DEVELOPMENT)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=['', 'test_string'])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_for_minimum_length_empty_then_valid(self, mock_print_red, mock_prompt):
        result = self.service.prompt_for_string_of_minimum_length("name", 2)
        mock_print_red.assert_called_once_with("'test_string' is not longer than 2 characters ")
        self.assertEqual(result, 'test_string')

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', return_value='valid_string')
    def test_prompt_for_valid_input_first_try_with_path(self, mock_prompt):
        result = self.service.prompt_for_string_of_minimum_length("name", 2)
        self.assertEqual(result, 'valid_string')

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=['a', 'valid_string'])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_for_short_input_then_valid(self, mock_print_red, mock_prompt):
        result = self.service.prompt_for_string_of_minimum_length("name", 2)
        mock_print_red.assert_called_once_with("'a' is not longer than 2 characters ")
        self.assertEqual(result, 'valid_string')

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=['a'*50, 'valid_string'])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_for_exceedingly_long_input_then_valid(self, mock_print_red, mock_prompt):
        result = self.service.prompt_for_string_of_minimum_length("name", 2)
        mock_print_red.assert_called_once_with(f"'{'a'*50}' is not longer than 2 characters ")
        self.assertEqual(result, 'valid_string')

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', return_value='ab')
    def test_prompt_for_exact_length(self, mock_prompt):
        result = self.service.prompt_for_string_of_minimum_length("name", 2)
        self.assertEqual(result, 'ab')

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=['a', 'ab', 'abc'])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_for_incrementing_lengths(self, mock_print_red, mock_prompt):
        result = self.service.prompt_for_string_of_minimum_length("name", 3)
        mock_print_red.assert_called_with("'ab' is not longer than 3 characters ")
        self.assertEqual(result, 'abc')

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', return_value='a'*100)
    def test_prompt_for_long_valid_input(self, mock_prompt):
        result = self.service.prompt_for_string_of_minimum_length("description", 50)
        self.assertEqual(result, 'a'*100)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=['', ''])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_for_continuous_empty_input(self, mock_print_red, mock_prompt):
        with self.assertRaises(StopIteration):
            self.service.prompt_for_string_of_minimum_length("name", 2)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=['a', 'b', 'c'])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_for_single_characters(self, mock_print_red, mock_prompt):
        result = self.service.prompt_for_string_of_minimum_length("name", 1)
        self.assertEqual(result, 'a')

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', return_value='test')
    def test_prompt_for_word_input(self, mock_prompt):
        result = self.service.prompt_for_string_of_minimum_length("word", 2)
        self.assertEqual(result, 'test')

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=['not_a_float', '5.5'])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_for_initial_estimate_invalid_then_valid(self, mock_print_red, mock_prompt):
        result = self.service.prompt_for_initial_estimate()
        mock_print_red.assert_called_once_with("not_a_float was not a valid number. ")
        self.assertEqual(result, 5.5)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', return_value='3.5')
    def test_prompt_for_initial_estimate_valid_first_try(self, mock_prompt):
        result = self.service.prompt_for_initial_estimate()
        self.assertEqual(result, 3.5)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=['', '4.0'])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_for_initial_estimate_empty_then_valid(self, mock_print_red, mock_prompt):
        result = self.service.prompt_for_initial_estimate()
        mock_print_red.assert_called_once_with(" was not a valid number. ")
        self.assertEqual(result, 4.0)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=['-1', '5.0'])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_for_initial_estimate_negative_then_valid(self, mock_print_red, mock_prompt):
        result = self.service.prompt_for_initial_estimate()
        mock_print_red.assert_called_once_with("-1 was not a valid number. ")
        self.assertEqual(result, 5.0)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=['1/2', '6.0'])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_for_initial_estimate_fraction_then_valid(self, mock_print_red, mock_prompt):
        result = self.service.prompt_for_initial_estimate()
        mock_print_red.assert_called_once_with("1/2 was not a valid number. ")
        self.assertEqual(result, 6.0)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', return_value='0.5')
    def test_prompt_for_initial_estimate_valid_fraction(self, mock_prompt):
        result = self.service.prompt_for_initial_estimate()
        self.assertEqual(result, 0.5)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=['1,2', '7.0'])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_for_initial_estimate_comma_then_valid(self, mock_print_red, mock_prompt):
        result = self.service.prompt_for_initial_estimate()
        mock_print_red.assert_called_once_with("1,2 was not a valid number. ")
        self.assertEqual(result, 7.0)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', return_value='0.0')
    def test_prompt_for_initial_estimate_zero(self, mock_prompt):
        result = self.service.prompt_for_initial_estimate()
        self.assertEqual(result, 0.0)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=['.', '8.0'])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_for_initial_estimate_only_dot_then_valid(self, mock_print_red, mock_prompt):
        result = self.service.prompt_for_initial_estimate()
        mock_print_red.assert_called_once_with(". was not a valid number. ")
        self.assertEqual(result, 8.0)

    @patch('services.tickets.ticket_input_validation_service.prompt_underline', side_effect=['1.2.3', '9.0'])
    @patch('services.tickets.ticket_input_validation_service.print_red')
    def test_prompt_for_initial_estimate_too_many_dots_then_valid(self, mock_print_red, mock_prompt):
        result = self.service.prompt_for_initial_estimate()
        mock_print_red.assert_called_once_with("1.2.3 was not a valid number. ")
        self.assertEqual(result, 9.0)

    @patch('services.tickets.ticket_input_validation_service.prompt_and_validate_priority', return_value='1')
    @patch('services.tickets.ticket_input_validation_service.prompt_and_validate_ticket_type', return_value='Development')
    @patch('services.tickets.ticket_input_validation_service.prompt_for_string_of_minimum_length', side_effect=['Valid Ticket Name', 'Valid Ticket Description Longer Than Twenty Five Characters'])
    @patch('services.tickets.ticket_input_validation_service.prompt_for_initial_estimate', return_value=5.5)
    def test_generate_validated_user_ticket_inputs(self, mock_initial_estimate, mock_min_length, mock_ticket_type, mock_priority):
        result = self.service.generate_validated_user_ticket_inputs()
        
        # Assert that the mocked methods were called
        mock_priority.assert_called_once()
        mock_ticket_type.assert_called_once()
        mock_min_length.assert_has_calls([call('Ticket Name', 10), call('Ticket Description', 25)])
        mock_initial_estimate.assert_called_once()
        
        # Assert that the result is as expected
        self.assertEqual(result.priority, '1')
        self.assertEqual(result.ticket_type, 'Development')
        self.assertEqual(result.ticket_name, 'Valid Ticket Name')
        self.assertEqual(result.ticket_description, 'Valid Ticket Description Longer Than Twenty Five Characters')
        self.assertEqual(result.estimate, 5.5)
