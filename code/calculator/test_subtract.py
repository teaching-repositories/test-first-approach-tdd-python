import unittest
from calculator import subtract

class TestSubtract(unittest.TestCase):

    def test_subtract_integers(self):
        # Arrange
        num1 = 5
        num2 = 2

        # Act
        result = subtract(num1, num2)

        # Assert
        self.assertEqual(result, 3)

    def test_subtract_floats(self):
        # Arrange
        num1 = 7.5
        num2 = 3.5

        # Act
        result = subtract(num1, num2)

        # Assert
        self.assertAlmostEqual(result, 4.0)

    def test_subtract_string_integer_error(self):
        # Arrange
        str1 = "Hello"
        num2 = 2

        # Act & Assert
        with self.assertRaises(TypeError):
            subtract(str1, num2)

    def test_subtract_string_string_error(self):
        # Arrange
        str1 = "Hello"
        str2 = " World"

        # Act & Assert
        with self.assertRaises(TypeError):
            subtract(str1, str2)

if __name__ == "__main__":
    unittest.main()