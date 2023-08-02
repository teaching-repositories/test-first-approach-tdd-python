import unittest
from calculator import multiply

class TestMultiply(unittest.TestCase):

    def test_multiply_integers(self):
        # Arrange
        num1 = 2
        num2 = 3

        # Act
        result = multiply(num1, num2)

        # Assert
        self.assertEqual(result, 6)

    def test_multiply_floats(self):
        # Arrange
        num1 = 2.5
        num2 = 4.0

        # Act
        result = multiply(num1, num2)

        # Assert
        self.assertAlmostEqual(result, 10.0)

    def test_multiply_string_integer(self):
        # Arrange
        str1 = "Hello"
        num2 = 3

        # Act
        result = multiply(str1, num2)

        # Assert
        self.assertEqual(result, "HelloHelloHello")

    def test_multiply_string_string_error(self):
        # Arrange
        str1 = "Hello"
        str2 = " World"

        # Act & Assert
        with self.assertRaises(TypeError):
            multiply(str1, str2)

if __name__ == "__main__":
    unittest.main()