---
title: Test-Driven Development of a Credit Card Validator in Python
format: pdf
---

Test-driven development (TDD) is a process for writing code that relies on first creating failing test cases, then writing just enough code to make those tests pass. This helps drive better code design and quality.

In this tutorial, we will follow a TDD workflow to create a credit card validator in Python that uses the Luhn algorithm to check if a card number is valid. 

## 1. Write the test class skeleton

First, import the `unittest` module and create a `TestCreditCardValidator` test case class that inherits from `unittest.TestCase`. 

This class will contain all our tests:

```python
import unittest

class TestCreditCardValidator(unittest.TestCase):
```

## 2. Write failing test methods

Next, add some test methods that will fail initially:

- `test_valid_cc()` validates a valid number 
- `test_invalid_cc()` validates an invalid number

Use assertTrue() and assertFalse() to test the expected result:

```python
    def test_valid_cc(self):
        valid_cc = "4012888888881881"
        result = validate_credit_card(valid_cc)
        self.assertTrue(result)

    def test_invalid_cc(self):
        invalid_cc = "1234432156780000"  
        result = validate_credit_card(invalid_cc)
        self.assertFalse(result)
```

These will fail because `validate_credit_card()` doesn't exist yet.

## 3. Implement validation function

Define the `validate_credit_card()` function to make the tests pass:

```python
def validate_credit_card(cc_number):
    # Luhn algorithm implementation
    return True
```

For now, just return True to make the tests pass.

## 4. Incrementally implement Luhn algorithm 

Gradually update `validate_credit_card()` to properly implement the Luhn algorithm:

- Sum the digits, doubling every other one
- Return True if the sum modulo 10 is 0 

Run tests frequently to ensure each change makes them pass.

```python
def validate_credit_card(cc_number):
    checksum = 0
    for i in range(len(cc_number)):
        digit = int(cc_number[i])
        if i % 2 == 0:
            digit *= 2
        checksum += digit // 10 + digit % 10
    return checksum % 10 == 0
```

## 5. Refactor for readability

Once the implementation is complete, refactor to improve code quality:

- Extract sum calculation into `_sum_digits()` helper
- Use more descriptive variable names
- Add comments explaining the algorithm

Rerun tests after each change to catch any regressions.

## Summary

By using TDD with `unittest`, we drive the development of a well-tested credit card validator that uses the Luhn algorithm. The tests provide safety nets during refactoring to prevent regressions.



