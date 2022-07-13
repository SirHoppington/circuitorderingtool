from flask import request, json
import requests
import json
import pandas as pd
from app.utilities import btw_api_body, btw_api_body_fttc, add_quote_item
from app.queries import add_btw_quote
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

    # fetch quote via provider API.
    def quote_api(self, body):
        api_url = self.url + self.quote_url
        response = requests.post(api_url, headers=self.headers, data=json.dumps(body), auth=self.auth, verify=False)
        return response

     # retrieve existing quote using reference via Provider API.
    def retrieve_quote_api(self, quote_reference):
        api_url = self.url + self.retrieve_quote_url + str(quote_reference)
        response = requests.get(api_url, auth=self.auth)
        return response

        # Receive form details and run quote_api method and return pricing.
    def get_quote(self, postcode, filters):
        print(filters)
        cleansed_form = {k: v for k, v in filters.items() if v != ['Any'] and k != 'csrf_token' and k != 'postcode' and k != 'customer_email' and k != 'customer_name'}
        body = {"postcode": postcode, "filter": cleansed_form}
        response = self.quote_api(body)
        #product_pricing = json_to_panda_v1(response)
        return response
        #return product_pricing

        # take reference and run retrieve_quote_api method  and return pricing.
    #def fetch_quote(self, quote_reference):
    #    response = self.retrieve_quote_api(quote_reference)
    #    panda_pricing = json_to_panda_v1(response)
    #    return panda_pricing

    # Cleanse NewOrder form.
    def create_order(self, filter):
        start_cleansed_form = {k: v for k, v in filter.items() if k == 'quoteReference' or k ==
                         'pricingRequestHardwareId' or k == 'pricingRequestAccessProductId' or k == 'purchaseOrderNumber'}
        middle_cleansed_form = { k: v for k, v in filter.items() if k == 'FirstName' or
                         k == 'LastName' or k == 'Telephone' or
                         k == 'Email'}
        end_cleansed_form = {k: v for k, v in filter.items() if v != [
            'Any'] and k != 'csrf_token' and k != 'FirstName' and
                         k != 'LastName' and k != 'Telephone' and
                         k != 'Email' and k != 'quoteReference' and k !=
                         'pricingRequestHardwareId' and k != 'pricingRequestAccessProductId' and k != 'purchaseOrderNumber'}
        customer_contact = {"primaryProvisioningContact" : middle_cleansed_form}
        body = {**start_cleansed_form, **customer_contact, **end_cleansed_form}
        print(body)
        response = self.send_order(body)
        return response

    # Send cleansed order to 3rd Party order API.
    def send_order(self, body):
        api_url = self.url + self.order_url
        response = requests.get(api_url, headers=self.headers, data=json.dumps(body), auth=self.auth, verify=False)
        print(response)
        return response

class BasicProvider(Provider):
    def __init__(self, name, url, quote_url, retrieve_quote_url, order_url, address_lookup_url, username, password):
        self.auth = requests.auth.HTTPBasicAuth(username, password)
        self.address_lookup_url = address_lookup_url
        super().__init__(name, url, quote_url, retrieve_quote_url, order_url)

    def search_address(self, postcode):
        api_url = self.url + self.address_lookup_url
        response = requests.get(api_url, headers=self.headers, data={"postcode" : postcode }, auth=self.auth, verify=False)
        return response

class OAuthProvider(Provider):
    token = "test"
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
        self.token = token['access_token']
        print(self.token)

    def quote_api(self, body):

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.token,
            "APIGW-Tracking-Header": "96bb97fa-b941-46bb-8c4e-86c616c28a15"
        }
        print(headers)
        api_url = self.url + self.quote_url
        response = requests.post(api_url, headers=headers, json = body)
        return response
    #add a decision to check if accessTypes is Fibre or FTTC.
    def get_quote(self, postcode, bandwidths, filters):
        #quote_list = {"quoteItem": []}
        #iterate through bandwidths, map to BTW value and add a new quoteItem to JSON
        # add if bandwidth == [] and if product == FTTC then add new line for FTTC product
        quote_list = {"quoteItem": []}
        for type in filters["accessTypes"]:
            if type == "Fibre":
                product = "EtherwayFibreService"
                for bandwidth in filters["bandwidths"]:
                    if bandwidth == 'FROM_10_TO_100':
                        bw = '100 Mbit/s'
                        quote_list = add_quote_item(quote_list, filters, bw, product)
                    elif bandwidth == 'FROM_100_TO_1000':
                        bw = '100 Mbit/s'
                        quote_list = add_quote_item(quote_list, filters, bw, product)
                        bw = '1 Gbit/s'
                        quote_list = add_quote_item(quote_list, filters, bw, product)
                    elif bandwidth == 'FROM_1000_TO_10000':
                        bw = '1 Gbit/s'
                        quote_list = add_quote_item(quote_list, filters, bw, product)
                        bw = '10 Gbit/s'
                        quote_list = add_quote_item(quote_list, filters, bw, product)
                else:
                    product = "EtherwayGEAService"
                    for bandwidth in filters["bandwidths"]:
                        if bandwidth == 'FROM_10_TO_100':
                            bw = 'FTTC 40:10 Mbit/s'
                            quote_list = add_quote_item(quote_list, filters, bw, product)
                            bw = 'FTTC 80:20 Mbit/s'
                            quote_list = add_quote_item(quote_list, filters, bw, product)
            #else:
            #   product = "EtherwayGEAService"
            #    add_bandwidth(filters,bw, product)
        response = self.quote_api(quote_list)
        return response

v1_api =BasicProvider("Virtual 1", "https://apitest.virtual1.com/",
                  "layer2-api/quoting", "layer2-api/retrieveQuote?quoteReference=",
                  "layer2-api/orderingV2", "address-lookup", "apiuser@capita.co.uk", "EyNoe*Vr")

btw_test_api = OAuthProvider("BT Wholesale", "https://api-testa.business.bt.com/tmf-api/quoteManagement/v4",
                        "/quote", "/quote", "no_order",
                        "ErWw3KjIAjvtQVl6ZG3Gn1S3kGEAijpg","YZA99v6Ci9qSHTYY", "https://api-testa.business.bt.com/oauth/accesstoken")