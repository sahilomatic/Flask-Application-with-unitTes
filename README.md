# Flask-Application-with-unitTest
A payment System with unit test covering concept of mocking


1) src folder contains Flask application
2) Following is folder structure
      -src 
        -apis
           -urls.py
           - views,py
        -models
        -payments
           -cheap_payment.py
           -expensive_payment.py
           -premium_payment.py
           -user_service.py
           -validations.py
        -test_cases
           -test_validations.py
        -app.py
        
        
        
3) app.py is the main Flask application file . Both Function based views and Classed base views are implemented
4) from REST API , request goes to payments.user_service.UserService.process_payment function
5) payments.user_service.UserService.process_payment function performs certain validation based on following rules

6)  CreditCardNumber (mandatory, string, it should be a valid credit card number)
- CardHolder: (mandatory, string)
- ExpirationDate (mandatory, DateTime, it cannot be in the past)
- SecurityCode (optional, string, 3 digits)
- Amount (mandatoy decimal, positive amount)


7) For Validating Credit Card Number Luhn ALgoritm is used

8) If everything is valid, following actions are performed

9) The payment gateway that should be used to process each payment follows the next set of
    business rules:
    a) If the amount to be paid is less than £20, use CheapPaymentGateway.
    b) If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
    Otherwise, retry only once with CheapPaymentGateway.
    c) If the amount is > £500, try only PremiumPaymentGateway and retry up to 3 times
    in case payment does not get processed.
10) Test cases are made for Validation rule.
11) For payment gateways , sdk can be used of vrious companies liek RazorPay, Paytm etc.
