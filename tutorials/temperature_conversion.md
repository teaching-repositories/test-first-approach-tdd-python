---
title: TDD Temperature Conversion
format: pdf
---

Here is an outline of the TDD process in Python to test temperature conversion functions:

1. Write a test case for a Celsius to Fahrenheit conversion:

```python
import unittest

class TestTemperatureConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        celsius = 0
        expected = 32
        actual = celsius_to_fahrenheit(celsius)
        self.assertEqual(expected, actual)
```

2. Run the test and see it fail since the conversion function doesn't exist yet.

3. Write the minimum amount of code to make the test pass:

```python
def celsius_to_fahrenheit(celsius):
    return 32
```

4. Run the tests again and see it pass. 

5. Write another failing test, this time for a Fahrenheit to Celsius conversion:

```python 
    def test_fahrenheit_to_celsius(self):
        fahrenheit = 32
        expected = 0
        actual = fahrenheit_to_celsius(fahrenheit)
        self.assertEqual(expected, actual)
```

6. Run the tests and see the new one fail.

7. Write the minimum code to make it pass:

```python
def fahrenheit_to_celsius(fahrenheit):
    return 0
``` 

8. Run tests and they should now all pass.

9. Refactor as needed, running tests after each change to ensure they still pass.

10. Add more test cases to cover additional scenarios.

11. Repeat TDD process as needed!