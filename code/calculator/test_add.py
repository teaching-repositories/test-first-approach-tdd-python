import unittest
from calculator import add

class TestAdd(unittest.TestCase):

    def test_add_integers(self):
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

    def test_add_floats(self):
        # Arrange
        num1 = 2.5
        num2 = 3.5

        # Act
        result = add(num1, num2)

        # Assert
        self.assertAlmostEqual(result, 6.0)

    def test_add_string_integer_error(self):
        # Arrange
        num1 = "two"
        num2 = 2

        # Act 
        def action():
            add(num1, num2)

        # Assert
        self.assertRaises(TypeError, action)
            

    def test_add_string_concatenation(self):
        # Arrange
        str1 = "Hello"
        str2 = " World"

        # Act
        result = add(str1, str2)

        # Assert
        self.assertEqual(result, "Hello World")    
    
 
if __name__ == "__mßain__":
    unittest.main()