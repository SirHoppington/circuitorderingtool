from flask import request, json
import requests
import json
import pandas as pd
from app.utilities import json_to_panda_v1
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth

class Provider:

    headers = {
        "Content-Type": "application/json"
    }

    auth = "basic"

    def __init__(self,name, url, quote_url, retrieve_quote_url, order_url):
        self.name = name
        self.url = url
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
        print(filters)
        cleansed_form = {k: v for k, v in filters.items() if v != ['Any'] and k != 'csrf_token' and k != 'postcode' and k != 'customer_email' and k != 'customer_name'}
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

class BasicProvider(Provider):
    def __init__(self, name, url, quote_url, retrieve_quote_url, order_url, username, password):
        self.auth = requests.auth.HTTPBasicAuth(username, password)
        super().__init__(name, url, quote_url, retrieve_quote_url, order_url)

class OAuthProvider(Provider):

    def __init__(self,name, url , quote_url, retrieve_quote_url, order_url, client_id, client_secret, authorization_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authorization_url = authorization_url
        super().__init__(name, url, quote_url, retrieve_quote_url, order_url)

    def fetch_access_token(self):
        auth1 = HTTPBasicAuth(self.client_id, self.client_secret)
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        # token should be used in auth header
        token = oauth.fetch_token(token_url=self.authorization_url, auth=auth1)
        auth = token
        print(auth)

v1_api =BasicProvider("Virtual 1", "https://apitest.virtual1.com/",
                  "layer2-api/quoting", "layer2-api/retrieveQuote?quoteReference=",
                  "layer2-api/ordering", "apiuser@capita.co.uk", "EyNoe*Vr")

btw_test_api = OAuthProvider("BT Wholesale", "https://api-testa.business.bt.com/tmf-api/quoteManagement/v4",
                        "quote", "quote", "no_order",
                        "ErWw3KjIAjvtQVl6ZG3Gn1S3kGEAijpg","YZA99v6Ci9qSHTYY", "https://api-testa.business.bt.com/oauth/accesstoken")