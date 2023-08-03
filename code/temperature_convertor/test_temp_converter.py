import unittest
from temp_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

class TestTemperatureConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        # Arrange
        celsius = 0
        expected = 32

        # Act
        actual = celsius_to_fahrenheit(celsius)

        # Assert
        self.assertEqual(expected, actual)

    def test_fahrenheit_to_celsius(self):
        # Arrange
        fahrenheit = 32
        expected = 0

        # Act
        actual = fahrenheit_to_celsius(fahrenheit)

        # Assert
        self.assertEqual(expected, actual)
    
    def test_celsius_to_fahrenheit_freezing(self):
        # Arrange
        celsius = 0
        expected = 32

        # Act
        actual = celsius_to_fahrenheit(celsius)
        
        # Assert
        self.assertEqual(expected, actual)

    def test_fahrenheit_to_celsius_boiling(self):
        # Arrange
        fahrenheit = 212
        expected = 100

        # Act
        actual = fahrenheit_to_celsius(fahrenheit)
        
        # Assert
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()