import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def test_add_two_numbers(self):
      # Arrange
      num1 = 5 
      num2 = 3

      # Act
      result = add(num1, num2)

      # Assert
      self.assertEqual(result, 8)

      # Arrange
      num1 = 2
      num2 = 4

      # Act
      result = add(num1, num2)

      # Assert
      self.assertEqual(result, 6)

      # Arrange
      num1 = 0
      num2 = 1

      # Act
      result = add(num1, num2)

      # Assert
      self.assertEqual(result, 1)
  

if __name__ == "__main__":
    unittest.main()