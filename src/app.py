from __future__ import absolute_import, unicode_literals
from flask import Flask,request,json,jsonify
from payments import UserService
import os
import logging.config



application = Flask(__name__)


with application.app_context():
    # this loads all the views with the app context
    # this is also helpful when the views import other
    # modules, this will load everything under the application
    # context and then one can use the current_app configuration
    # parameters
    from apis.urls import all_urls
    from scripts import ALL_CLI_COMMANDS

    for cli_name, cli_command in ALL_CLI_COMMANDS.items():
        application.cli.add_command(cli_command, name=cli_name)


# Adding all the url rules in the api application
# Class based Views are commented as not required
#
for url, view, methods, _ in all_urls:
    application.add_url_rule(url, view_func=view, methods=methods)




# REST API , post method using route decorators i.e. function view
# Method View used as their is only 1 API
@application.route('/payment', methods=["GET","POST"])
def payments():
    print("Checking the Payment logger")
    if(request.method == 'POST'):
        data = request.get_json()
        obj = json.load(data)
        CreditCardNumber = obj['CreditCardNumber']
        CardHolder = obj['CardHolder']
        ExpirationDate = obj['ExpirationDate']
        SecurityCode = obj['SecurityCode']
        Amount = obj['Amount']


        return jsonify(UserService().process_payment(CreditCardNumber,CardHolder,ExpirationDate,Amount,SecurityCode))





if __name__ =='__main__':
    application.run(debug=True, port=5000)  # run app in debug mode on port 5000