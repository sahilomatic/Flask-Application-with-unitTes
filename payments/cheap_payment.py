class CheapPaymentGateway:
    def __init__(self, CreditCardNumber, CardHolder, ExpirationDate,
                 SecurityCode, Amount):
        self.credit_card_number = CreditCardNumber
        self.card_holder = CardHolder
        self.expiration_date = ExpirationDate
        self.security_code = SecurityCode
        self.amount = Amount

    def process_payment(self):
        print('used CheapPaymentGateway')
        return True