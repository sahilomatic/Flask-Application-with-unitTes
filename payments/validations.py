from datetime import datetime, timedelta

class Validation:


    def validate_request(self,CreditCardNumber,CardHolder,ExpirationDate,SecurityCode,Amount):
        """
           Validate received parameters

           Args:
               CreditCardNumber (str): CreditCardNumber (mandatory, string, it should be a valid credit card number)
               CardHolder (str): CardHolder: (mandatory, string)
               ExpirationDate (str): ExpirationDate (mandatory, DateTime, it cannot be in the past)
               SecurityCode (str): SecurityCode (optional, string, 3 digits)
               Amount (float): Amount (mandatoy decimal, positive amount)

           Returns:
               is_valid (bool): True or False based on validation
           """


        is_valid = False
        is_valid_expiration_date = self.is_valid_expiration_date(ExpirationDate)
        is_valid_credit_card_holder = self.is_valid_credit_card_holder(CardHolder)
        is_valid_amount = self.is_valid_amount(Amount)
        is_valid_security_code = self.is_valid_security_code(SecurityCode)
        is_valid_credit_card_number = self.is_valid_credit_card_number(CreditCardNumber)
        print(is_valid_expiration_date ,is_valid_credit_card_holder,is_valid_amount,is_valid_security_code,
              is_valid_credit_card_number)
        if(is_valid_expiration_date
                and is_valid_credit_card_holder
                and is_valid_amount
                and is_valid_security_code
                and is_valid_credit_card_number
            ):
            is_valid = True

        return is_valid


    def is_valid_expiration_date(self, expiration_date):
        """
           Validate expiration_date

           Args:

               ExpirationDate (str): ExpirationDate (mandatory, DateTime, it cannot be in the past)


           Returns:
               is_valid (bool): True or False based on validation
           """


        today = datetime.now()
        is_valid = False
        print(isinstance(expiration_date,datetime))
        if((isinstance(expiration_date,datetime)) and (expiration_date>today)):
            is_valid = True
        return is_valid


    def is_valid_credit_card_holder(self, card_holder):
        """
                   Validate card_holder

                   Args:

                       card_holder (str): CardHolder: (mandatory, string)


                   Returns:
                        (bool): True or False based on validation
                   """


        return (isinstance(card_holder,str))


    def is_valid_amount(self, amount):
        """
                   Validate received parameters

                   Args:

                       amount (float): Amount (mandatoy decimal, positive amount)

                   Returns:
                       is_valid (bool): True or False based on validation
                   """


        is_valid = False
        print('amount',amount)
        if ((isinstance(amount, float)) and (amount > 0)):
            is_valid = True
        return is_valid


    def is_valid_security_code(self, security_code):

        """
                  Validate received security_code

                  Args:

                      security_code (str): SecurityCode (optional, string, 3 digits)


                  Returns:
                      is_valid (bool): True or False based on validation
                  """


        is_valid = False
        if(security_code is None):
            is_valid = True
        if ((isinstance(security_code, str)) and (len(security_code)==3) and (security_code.isdigit())):
            is_valid = True
        return is_valid

    def is_valid_credit_card_number(self,card_number):

        """
                   Validate received card_number. Credit Card Number validation is done on the basis of Luhn Algorithm.

                   Args:
                       card_number (str): CreditCardNumber (mandatory, string, it should be a valid credit card number)


                   Returns:
                       is_valid (bool): True or False based on validation
                   """




        'Based on Luhn Algorithm'
        card_number = list(card_number)

        # Remove the last digit from the card number
        check_digit = card_number.pop()

        # Reverse the order of the remaining numbers
        card_number.reverse()

        processed_digits = []

        for index, digit in enumerate(card_number):
            if index % 2 == 0:
                doubled_digit = int(digit) * 2

                # Subtract 9 from any results that are greater than 9
                if doubled_digit > 9:
                    doubled_digit = doubled_digit - 9

                processed_digits.append(doubled_digit)
            else:
                processed_digits.append(int(digit))

        total = int(check_digit) + sum(processed_digits)

        # Verify that the sum of the digits is divisible by 10
        if total % 10 == 0:
            return True
        else:
            return False


if __name__ =='__main__':
    obj = Validation()
    print('abc123'.isdigit())