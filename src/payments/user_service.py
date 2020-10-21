from payments.validations import Validation
from datetime import datetime,timedelta
from payments.premium_payment import PremiumPaymentGateway
from payments.expensive_payment import ExpensivePaymentGateway
from payments.cheap_payment import CheapPaymentGateway


class UserService(object):


    def process_payment(self,CreditCardNumber,CardHolder,ExpirationDate,Amount,SecurityCode=None):
        """
           User Payment Service.
           Validates code and then pass for selecting payment method

           Args:
               CreditCardNumber (str): CreditCardNumber (mandatory, string, it should be a valid credit card number)
               CardHolder (str): CardHolder: (mandatory, string)
               ExpirationDate (str): ExpirationDate (mandatory, DateTime, it cannot be in the past)
               SecurityCode (str): SecurityCode (optional, string, 3 digits)
               Amount (float): Amount (mandatoy decimal, positive amount)

           Returns:
               response: The response of this method should be 1 of the followings based on
                            - Payment is processed: 200 OK
                            - The request is invalid: 400 bad request
                            - Any error: 500 internal server error
           """
        response = None
        try:

            # check valid CreditCardNumber
            is_valid = Validation().validate_request(CreditCardNumber,CardHolder,ExpirationDate,SecurityCode,Amount)
            if(is_valid):
                if(self.select_payment(CreditCardNumber,CardHolder,ExpirationDate,SecurityCode,Amount)):
                    response = ("Payment is processed: 200 OK", 200)
            else:
                response = ("The request is invalid: 400 bad request",400)


        except Exception:
            response = ("Any error: 500 internal server error", 500)



        return response






    def select_payment(self,CreditCardNumber,CardHolder,ExpirationDate,SecurityCode,Amount):
        """
                   The payment gateway that should be used to process each payment follows the next set of
                        business rules:
                        a) If the amount to be paid is less than £20, use CheapPaymentGateway.
                        b) If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
                        Otherwise, retry only once with CheapPaymentGateway.
                        c) If the amount is > £500, try only PremiumPaymentGateway and retry up to 3 times
                        in case payment does not get processed.

                   Args:
                       CreditCardNumber (str): CreditCardNumber (mandatory, string, it should be a valid credit card
                       number)
                       CardHolder (str): CardHolder: (mandatory, string)
                       ExpirationDate (str): ExpirationDate (mandatory, DateTime, it cannot be in the past)
                       SecurityCode (str): SecurityCode (optional, string, 3 digits)
                       Amount (float): Amount (mandatoy decimal, positive amount)

                   Returns:
                       response: The response of this method should be 1 of the followings based on
                                    - Payment is processed: 200 OK
                                    - The request is invalid: 400 bad request
                                    - Any error: 500 internal server error
                   """
        response = None
        if(Amount<=20):
            '''If the amount to be paid is less than £20, use CheapPaymentGateway.'''
            response = self.process_cheap_payment(CreditCardNumber,CardHolder,ExpirationDate,SecurityCode,Amount)
        elif(Amount>=21 and Amount<=500):
            '''If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
            Otherwise, retry only once with CheapPaymentGateway.'''
            response = self.process_expensive_payment(CreditCardNumber,CardHolder,ExpirationDate,SecurityCode,Amount)
        elif(Amount>500):
            '''If the amount is > £500, try only PremiumPaymentGateway and retry up to 3 times
                in case payment does not get processed.'''
            response = self.process_premium_payment(CreditCardNumber,CardHolder,ExpirationDate,SecurityCode,Amount)

        return response




    def process_cheap_payment(self,CreditCardNumber,CardHolder,ExpirationDate,SecurityCode,Amount):

        """
                           Dummy code for CheapPaymentGateway

                           Args:
                               CreditCardNumber (str): CreditCardNumber (mandatory, string, it should be a valid credit card
                               number)
                               CardHolder (str): CardHolder: (mandatory, string)
                               ExpirationDate (str): ExpirationDate (mandatory, DateTime, it cannot be in the past)
                               SecurityCode (str): SecurityCode (optional, string, 3 digits)
                               Amount (float): Amount (mandatoy decimal, positive amount)

                           Returns:
                               payment_success_bool (bool): True or False value based on payment success
                           """


        payment_success_bool = CheapPaymentGateway(CreditCardNumber,CardHolder,ExpirationDate,
                                              SecurityCode,Amount).process_payment()

        return payment_success_bool




    def process_expensive_payment(self,CreditCardNumber,CardHolder,ExpirationDate,SecurityCode,Amount):
        """
           If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
            Otherwise, retry only once with CheapPaymentGateway.

           Args:
               CreditCardNumber (str): CreditCardNumber (mandatory, string, it should be a valid credit card
               number)
               CardHolder (str): CardHolder: (mandatory, string)
               ExpirationDate (str): ExpirationDate (mandatory, DateTime, it cannot be in the past)
               SecurityCode (str): SecurityCode (optional, string, 3 digits)
               Amount (float): Amount (mandatoy decimal, positive amount)

           Returns:
               payment_success_bool (bool): True or False value based on payment success
                                   """


        payment_success_bool = ExpensivePaymentGateway(CreditCardNumber,CardHolder,ExpirationDate,
                                                  SecurityCode,Amount).process_payment()
        if(not payment_success_bool):
            payment_success_bool = CheapPaymentGateway(CreditCardNumber,CardHolder,ExpirationDate,
                                                  SecurityCode,Amount).process_payment()
        return payment_success_bool

    def process_premium_payment(self,CreditCardNumber,CardHolder,ExpirationDate,SecurityCode,Amount):

        """
                If the amount is > £500, try only PremiumPaymentGateway and retry up to 3 times
                in case payment does not get processed.

       Args:
           CreditCardNumber (str): CreditCardNumber (mandatory, string, it should be a valid credit card
           number)
           CardHolder (str): CardHolder: (mandatory, string)
           ExpirationDate (str): ExpirationDate (mandatory, DateTime, it cannot be in the past)
           SecurityCode (str): SecurityCode (optional, string, 3 digits)
           Amount (float): Amount (mandatoy decimal, positive amount)

       Returns:
           payment_success_bool (bool): True or False value based on payment success
       """




        request_count = 0
        payment_success_bool = False

        while((not payment_success_bool) and request_count<3):
            payment_success_bool = PremiumPaymentGateway(CreditCardNumber,CardHolder,
                                                    ExpirationDate,SecurityCode,Amount).process_payment()
            request_count = request_count + 1

        return payment_success_bool

if __name__=='__main__':
     CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount = ['5893804115457289','Sahil Soni',
                                                                           datetime.now()+timedelta(2),25.0,'876']
     print(UserService().process_payment(CreditCardNumber,CardHolder,ExpirationDate,SecurityCode,Amount))