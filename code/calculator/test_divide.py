import unittest
from calculator import divide

class TestDivide(unittest.TestCase):

    def test_divide_normal(self):
        # Arrange
        num1 = 10
        num2 = 2

        # Act
        result = divide(num1, num2)

        # Assert
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        # Arrange
        num1 = 10
        num2 = 0

        # Act & Assert
        with self.assertRaises(ZeroDivisionError):
            divide(num1, num2)

    def test_divide_float(self):
        # Arrange
        num1 = 10.0
        num2 = 3.0

        # Act
        result = divide(num1, num2)

        # Assert
        self.assertAlmostEqual(result, 3.33333, places=5)

    def test_divide_non_number(self):
        # Arrange
        num1 = "ten"
        num2 = 2

        # Act & Assert
        with self.assertRaises(TypeError):
            divide(num1, num2)

if __name__ == "__main__":
    unittest.main()