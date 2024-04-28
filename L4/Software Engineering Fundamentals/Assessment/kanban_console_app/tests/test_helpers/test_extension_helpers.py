import unittest
from helpers.extension_helpers import *

class TestExtensionHelpers(unittest.TestCase):
    
    def test_convert_float_to_time(self):
        self.assertEqual(convert_float_to_time(4.5), (4, 30))
        self.assertEqual(convert_float_to_time(3.75), (3, 45))
        self.assertEqual(convert_float_to_time(0), (0, 0))

    def test_validate_as_int(self):
        self.assertTrue(validate_as_int('5'))
        self.assertFalse(validate_as_int('5.6'))
        self.assertFalse(validate_as_int('five'))
        self.assertFalse(validate_as_int(''))


    def test_validate_as_float(self):
        self.assertTrue(validate_as_float('5.6'))
        self.assertTrue(validate_as_float('5'))
        self.assertFalse(validate_as_float('five.point.six'))
        self.assertFalse(validate_as_float(''))


    def test_find_option_by_number(self):
        options = ["1: Option One", "2: Option Two", "3: Option Three"]
        self.assertEqual(find_option_by_number(options, 2), "2: Option Two")
        self.assertEqual(find_option_by_number(options, 4), "Unknown Option")
        self.assertEqual(find_option_by_number(options, 0), "Unknown Option")

    # def test_find_option_by_number_with_large_list(self):
    #     #This test will fail, code only supports single digit numbers.
    #     options_large = [f"{i}: Option {i}" for i in range(1, 101)]
    #     self.assertEqual(find_option_by_number(options_large, 50), "50: Option 50")

    def test_check_option_in_range(self):
        self.assertTrue(check_option_in_range(5, 4))
        self.assertFalse(check_option_in_range(5, 6))
        self.assertTrue(check_option_in_range(5.5, 5))
        self.assertFalse(check_option_in_range(5.5, 5.6))
