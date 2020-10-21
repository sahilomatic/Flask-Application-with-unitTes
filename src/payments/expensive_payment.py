class ExpensivePaymentGateway:
    ''' respective software development kit of companies can be used , which will involve 
    methods like creating connection with API , login into system using credential and 
    perform transaction'''
    def __init__(self, CreditCardNumber, CardHolder, ExpirationDate,
                 SecurityCode, Amount):
        self.credit_card_number = CreditCardNumber
        self.card_holder = CardHolder
        self.expiration_date = ExpirationDate
        self.security_code = SecurityCode
        self.amount = Amount


    def process_payment(self):
        print('used ExpensivePaymentGateway')
        return True
