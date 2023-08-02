import unittest
from temp_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

class TestTemperatureConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        celsius = 0
        expected = 32
        actual = celsius_to_fahrenheit(celsius)
        self.assertEqual(expected, actual)

    def test_fahrenheit_to_celsius(self):
        fahrenheit = 32
        expected = 0
        actual = fahrenheit_to_celsius(fahrenheit)
        self.assertEqual(expected, actual)
    
    def test_celsius_to_fahrenheit_freezing(self):
        celsius = 0
        expected = 32
        actual = celsius_to_fahrenheit(celsius)
        self.assertEqual(expected, actual)

    def test_fahrenheit_to_celsius_boiling(self):
        fahrenheit = 212
        expected = 100
        actual = fahrenheit_to_celsius(fahrenheit)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()