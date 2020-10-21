import logging
from flask import request,json,jsonify
from flask.views import MethodView
from payments.user_service import UserService

logger = logging.getLogger("default")
'''Flask REST API using pluggable classes'''
class Payments(MethodView):
    def post(self):
        logger.info("Checking the Payment logger")
        data = request.get_json()
        obj = json.load(data)
        CreditCardNumber = obj['CreditCardNumber']
        CardHolder = obj['CardHolder']
        ExpirationDate = obj['ExpirationDate']
        SecurityCode = obj['SecurityCode']
        Amount = obj['Amount']
        return jsonify(UserService().process_payment(CreditCardNumber,CardHolder,ExpirationDate,Amount,SecurityCode))
