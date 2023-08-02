import unittest
from validators import validate_password

class TestPasswordValidator(unittest.TestCase):

    def test_password_too_short(self):
        password = "foo"
        result = validate_password(password)
        self.assertFalse(result, "Password is too short")

    def test_password_no_uppercase(self):
        password = "foobar" 
        result = validate_password(password)
        self.assertFalse(result, "Password must contain uppercase letters")

    def test_password_no_lowercase(self):
        password = "FOOBAR"
        result = validate_password(password)
        self.assertFalse(result, "Password must contain lowercase letters")

    def test_password_no_number(self):
        password = "FooBar"
        result = validate_password(password)
        self.assertFalse(result, "Password must contain a number")

    def test_password_no_special_char(self):
        password = "FooBar123"
        result = validate_password(password)
        self.assertFalse(result, "Password must contain a special character")

    def test_valid_password(self):
        password = "FooBar123!"
        result = validate_password(password)
        self.assertTrue(result, "Valid password")

    def test_empty_password(self):
        password = ""
        result = validate_password(password)
        self.assertFalse(result, "Password cannot be empty")

    def test_whitespace_only_password(self):
        password = " " 
        result = validate_password(password)
        self.assertFalse(result, "Password cannot contain only whitespace")

    def test_too_long_password(self):
        password = "a" * 31
        result = validate_password(password)
        self.assertFalse(result, "Password is too long")

if __name__ == '__main__':
    unittest.main()