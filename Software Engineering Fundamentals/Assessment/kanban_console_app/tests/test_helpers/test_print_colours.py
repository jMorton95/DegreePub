import sys
import unittest
from unittest.mock import patch
from helpers.print_colours import *
from io import StringIO


class TestPrintColours(unittest.TestCase):
    
    def setUp(self):
        # Redirect stdout and stderr to capture print outputs and input prompts
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        sys.stdout = self.held_output
        sys.stderr = self.held_output

    def tearDown(self):
        # Reset stdout and stderr back to their original states
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr

    def assertPrinted(self, color, message):
        # Assert that the expected colored message was printed
        self.held_output.seek(0)
        self.assertEqual(self.held_output.read(), color + message + Terminal.ENDC + '\n')

    def test_print_green(self):
        print_green("Hello Green")
        self.assertPrinted(Terminal.OKGREEN, "Hello Green")

    def test_print_red(self):
        print_red("Hello Red")
        self.assertPrinted(Terminal.FAIL, "Hello Red")

    def test_print_blue(self):
        print_blue("Hello Blue")
        self.assertPrinted(Terminal.OKBLUE, "Hello Blue")

    def test_print_yellow(self):
        print_yellow("Hello Yellow")
        self.assertPrinted(Terminal.WARNING, "Hello Yellow")

    def test_print_beige(self):
        print_beige("Hello Beige")
        self.assertPrinted(Terminal.HEADER, "Hello Beige")

    def test_prompt_underline(self):
      message = "Prompt Message"
      simulated_input = "User Input"
      
      with patch('builtins.input', return_value=simulated_input) as mock_input:
          result = prompt_underline(message)
          
          # Verify that mock input was called once.
          mock_input.assert_called_once()
          
          # Check what's in the held_output right after prompt_underline is called.
          self.held_output.seek(0)
          captured_output = self.held_output.read()
          print("Captured output:", captured_output)  # Temporarily print out the captured output

      # Continue with your existing checks.
      self.assertEqual(result, simulated_input)
      self.assertPrinted(Terminal.UNDERLINE, message)