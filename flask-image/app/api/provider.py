from flask import request, json
import requests
import json
import pandas as pd
from app.utilities import json_to_panda_v1

class Provider:

    headers = {
        "Content-Type": "application/json"
    }

    def __init__(self,name, url, username, password , quote_url, retrieve_quote_url, order_url):
        self.name = name
        self.url = url
        self.auth = requests.auth.HTTPBasicAuth(username, password)
        self.quote_url = quote_url
        self.retrieve_quote_url = retrieve_quote_url
        self.order_url = order_url

    # fetch quote API.
    def quote_api(self, body):
        api_url = self.url + self.quote_url
        response = requests.post(api_url, headers=self.headers, data=json.dumps(body), auth=self.auth, verify=False)
        return response

     # retrieve quote API.
    def retrieve_quote_api(self, quote_reference):
        api_url = self.url + self.retrieve_quote_url + str(quote_reference)
        response = requests.get(api_url, auth=self.auth)
        return response

        # Receive form details and send to API quote and return panda.
    def get_quote(self, postcode, filters):
        cleansed_form = {k: v for k, v in filters.items() if v != ['Any'] and k != 'csrf_token' and k != 'postcode'}
        body = {"postcode": postcode, "filter": cleansed_form}
        response = self.quote_api(body)
        #quote_pricing = quote_to_panda_v1(response)
        #product_pricing = product_to_panda_v1(response)
        product_pricing = json_to_panda_v1(response)
        # will save all panda to database table, likely best to only save quotation reference.
        # panda.to_sql(name='provider_pricing', con=db.engine, index=False)
        return product_pricing

        # Fetch quote via API and return as Panda.
    def fetch_quote(self, quote_reference):
        response = self.retrieve_quote_api(quote_reference)
        panda_pricing = json_to_panda_v1(response)
        return panda_pricing

        # Create new order.
    def create_order(self, order_details):
        response = requests.get(self.order_url, auth=self.basic)
        panda_pricing = json_to_panda_v1(response)
        return panda_pricing

v1_api = Provider("Virtual 1", "https://apitest.virtual1.com/",
                  "apiuser@capita.co.uk", "EyNoe*Vr", "layer2-api/quoting",
                  "layer2-api/retrieveQuote?quoteReference=", "layer2-api/ordering")
