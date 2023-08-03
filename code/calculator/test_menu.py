import unittest
from unittest.mock import patch
from calculator import display_menu, take_input, take_numbers_input, call_function

class TestMenu(unittest.TestCase):

    def test_display_menu(self):
        # Arrange
        expected_output = "1. Add\n2. Subtract\n3. Multiply\n4. Divide\n"
        
        # Act
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            display_menu()
        
        # Assert
        self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_take_input(self):
        # Arrange
        expected_input = '1'
        
        # Act
        with patch('builtins.input', return_value=expected_input):
            result = take_input()
        
        # Assert
        self.assertEqual(result, expected_input)

    def test_take_numbers_input(self):
        # Arrange
        expected_inputs = [3, 2]
        
        # Act
        with patch('builtins.input', side_effect=expected_inputs):
            result = take_numbers_input()
        
        # Assert
        self.assertEqual(result, tuple(expected_inputs))

    def test_call_function(self):
        # Arrange
        expected_inputs = ['1', '2', '3']
        expected_output = 5  # 2 + 3 = 5
        
        # Act
        with patch('builtins.input', side_effect=expected_inputs):
            result = call_function()
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_invalid_input(self):
        # Arrange
        invalid_input = '5'
        
        # Act
        with patch('builtins.input', return_value=invalid_input):
            result = call_function()
        
        # Assert
        self.assertEqual(result, "Invalid input")

if __name__ == "__main__":
    unittest.main()
