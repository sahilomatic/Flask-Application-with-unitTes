from mock import patch
import unittest

from payments.validations import Validation
from datetime import datetime,timedelta

class ValdatorTest(unittest.TestCase):

    def setUp(self):
        self.obj = Validation()
        self.credit_card_number, self.card_holder, self.expiration_date,\
        self.security_code, self.amount = ['5893804115457289', 'Sahil Soni', datetime.now() + timedelta(2), '876',
                                                                              1500.0]

    # Returns True or False.
    def test_is_valid_expiration_date(self):
        'ExpirationDate (mandatory, DateTime, it cannot be in the past)'
        # asserts True
        self.assertTrue(self.obj.is_valid_expiration_date(self.expiration_date))



        # asserts False , expiry date less than today date
        self.assertFalse(self.obj.is_valid_expiration_date(self.expiration_date - timedelta(50)))


    def test_is_valid_credit_card_holder(self):
        'SecurityCode (optional, string, 3 digits)'
        # asserts Security Code is string
        self.assertTrue(self.obj.is_valid_credit_card_holder(self.security_code))



        # asserts False , Security Code is digit
        self.assertFalse(self.obj.is_valid_credit_card_holder(123))
        
    def test_is_valid_amount(self):
        'Amount (mandatoy decimal, positive amount)'

        # asserts True
        self.assertTrue(self.obj.is_valid_amount(150.0))



        # asserts False , amount is string
        self.assertFalse(self.obj.is_valid_amount('123'))
        # asserts False , amount is int
        self.assertFalse(self.obj.is_valid_amount(123))
    
    def test_is_valid_security_code(self):
        'SecurityCode (optional, string, 3 digits)'

        # asserts True
        self.assertTrue(self.obj.is_valid_security_code(None))

        # asserts True
        self.assertTrue(self.obj.is_valid_security_code('123'))



        # asserts False , security code len is not 3
        self.assertFalse(self.obj.is_valid_security_code('1256'))
        # asserts False , security code is not str
        self.assertFalse(self.obj.is_valid_security_code(123))

        # asserts False , security code is not digit
        self.assertFalse(self.obj.is_valid_security_code('abc123'))
    
    
    def test_is_valid_credit_card_number(self):
        'CreditCardNumber (mandatory, string, it should be a valid credit card number)'

        # asserts True, valid credit card number passed
        self.assertTrue(self.obj.is_valid_credit_card_number(self.credit_card_number))



        # asserts False , invalid credit card number passed
        self.assertFalse(self.obj.is_valid_credit_card_number(self.credit_card_number[:7]))
        # asserts False , security code is not str
    


    @patch("payments.validations.Validation.is_valid_expiration_date")
    @patch("payments.validations.Validation.is_valid_credit_card_holder")
    @patch("payments.validations.Validation.is_valid_amount")
    @patch("payments.validations.Validation.is_valid_security_code")
    @patch("payments.validations.Validation.is_valid_credit_card_number")
    def test_validate_request(self,mock1,mock2,mock3,mock4,mock5):
        'validate_request return True when all properties are valid'




        'mocking with all function returning True, should assert True'


        mock1.return_value = True
        mock2.return_value = True
        mock3.return_value = True
        mock4.return_value = True
        mock5.return_value = True

        credit_card_number, card_holder, expiration_date, \
        security_code, amount = ['r1','r2','r3','r4','r5']
        # asserts True, valid credit card number passed
        self.assertTrue(self.obj.validate_request(credit_card_number, card_holder, expiration_date, \
        security_code, amount))

        'mocking with 1 function returning false, should assert False'

        mock1.return_value = True
        mock2.return_value = False
        mock3.return_value = True
        mock4.return_value = True
        mock5.return_value = True

        self.assertFalse(self.obj.validate_request(credit_card_number, card_holder, expiration_date, \
                                                  security_code, amount))
if __name__ == '__main__':
    unittest.main()