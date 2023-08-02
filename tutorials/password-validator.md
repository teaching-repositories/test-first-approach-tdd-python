---
title: # Test-Driven Development of a Password Validator with unittest
format: pdf
---

Test-driven development (TDD) is a process that relies on first writing failing tests, then writing just enough code to make those tests pass. It is very useful for improving code design and quality.

In this tutorial, we will follow a TDD workflow to develop a password validation function using Python's unittest framework.

## 1. Write a failing unittest

First, we need to write a test case and tests that will fail because the code does not exist yet.

Import unittest and create a TestPasswordValidator class that inherits from unittest.TestCase:

```python
import unittest

class TestPasswordValidator(unittest.TestCase):
```

Write a test method like test_too_short() that:

- Arranges the input password "foo"
- Calls validate_password() on that input 
- Asserts that result is False using self.assertFalse()

```python
    def test_too_short(self):
        password = "foo"
        result = validate_password(password)
        self.assertFalse(result)
```

This test will fail because we haven't implemented validate_password() yet. 

## 2. Write basic implementation

Now we can write just enough code to make this initial test pass:

- Implement validate_password()
- Check if password length is less than 8
- Return False if too short

```python
def validate_password(password):
    min_length = 8
    if len(password) < min_length:
        return False
```

Run the tests again and the first one should now pass!

## 3. Write more failing tests

Next, write more test methods that will fail for different validation criteria:

```python
    def test_missing_uppercase(self):
        # Test password with no uppercase
        
    def test_missing_lowercase(self):
        # Test password with no lowercase

    def test_missing_number(self):
        # Test password with no number

    def test_missing_special(self):
        # Test password with no special char
```

Run the tests again and they should all fail.

## 4. Incrementally make tests pass

One by one, update validate_password() to make each new test pass. 

Some things that could be added:

- Check password length
- Use regex to check for presence of character classes  
- Return False if any expected criteria is missing

Run tests after each change until all pass.

## 5. Refactor for readability and maintainability

Now that we have full test coverage, we can refactor validate_password() for better code quality:

- Split validation into separate helper functions
- Use a list of required character classes instead of individual checks
- Return as soon as an invalid case is found instead of checking everything

Rerun tests periodically to make sure refactoring does not break anything.

## Summary

By following TDD with unittest, we've built a robust password validation function from the ground up. The tests provide safety nets to catch any regressions during refactoring. unittest gives us shared fixtures and organization for readability.
