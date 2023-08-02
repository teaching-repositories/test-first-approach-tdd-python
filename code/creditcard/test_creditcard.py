import unittest
from creditcard import validate_credit_card

class TestCreditCardValidator(unittest.TestCase):

    def test_valid_credit_card(self):
        valid_cc = "4007702835532454"
        self.assertTrue(validate_credit_card(valid_cc))

    def test_invalid_credit_card(self):
        invalid_cc = "5541801923795241"
        self.assertFalse(validate_credit_card(invalid_cc))
    
    def test_non_digit_characters(self):
        invalid_cc = "5541-8019-2379-5241"
        self.assertFalse(validate_credit_card(invalid_cc))

    def test_empty_string(self):
        self.assertFalse(validate_credit_card(""))

    def test_too_long(self):
        invalid_cc = "55418019237952400001" 
        self.assertFalse(validate_credit_card(invalid_cc))

    def test_too_short(self):
        invalid_cc = "5541801"
        self.assertFalse(validate_credit_card(invalid_cc))

if __name__ == '__main__':
    unittest.main()