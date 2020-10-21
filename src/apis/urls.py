from apis import views

'''
Following class based views are commented as it is not required.
api_urls = [
    ("/payment", views.Payments.as_view('payments_api'), ["POST"], "flask payment processing index url")
]
'''

api_urls = []
other_urls = []

all_urls = api_urls + other_urls
