from flask import request, json
import requests
import json
import pandas as pd
from app.utilities import add_quote_item, btw_order_api_body
from app.queries import add_btw_quote
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from config import v1_user, v1_password, btw_secret, btw_client_id, btw_sandbox_client_id ,btw_sandbox_secret
from datetime import datetime

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
        print(response.content)
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
        access = datetime.strptime(filter["accessAvailableFrom"], "%Y-%m-%d").strftime("%Y/%m/%d")
        start_cleansed_form = {k: v for k, v in filter.items() if k == 'quoteReference' or k ==
                         'pricingRequestHardwareId' or k == 'pricingRequestAccessProductId' or k == 'purchaseOrderNumber'}
        end_cleansed_form = {k: v for k, v in filter.items() if v != [
            'Any'] and k != 'csrf_token' and k != 'FirstName' and k != 'accessAvailableFrom' and
                         k != 'LastName' and k != 'Telephone' and
                         k != 'Email' and k != 'quoteReference' and k !=
                         'pricingRequestHardwareId' and k != 'pricingRequestAccessProductId' and k != 'purchaseOrderNumber'}
        customer_contact = {
            "primaryProvisioningContact": {"firstName": filter["FirstName"], "lastName": filter["LastName"],
                                           "telephone": filter["Telephone"], "email": filter["Email"]}}
        body = {**start_cleansed_form, **customer_contact, "accessAvailableFrom":access, **end_cleansed_form }
        print(body)
        response = self.send_order(body)
        return response

    # Send cleansed order to 3rd Party order API.
    def send_order(self, body):
        api_url = self.url + self.order_url
        response = requests.post(api_url, headers=self.headers, data=json.dumps(body), auth=self.auth, verify=False)
        print(response)
        print(response.content)
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
    # don't repeat and move this to top of class.
    def __init__(self,name, url , quote_url, retrieve_quote_url, address_url,
                 qual_url, order_url, client_id, client_secret, authorization_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.address_url = address_url
        self.qual_url = qual_url
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

    def address_lookup(self, postcode):
        headers = {
            "Authorization": "Bearer " + self.token,
            "APIGW-Tracking-Header": "96bb97fa-b941-46bb-8c4e-86c616c28a15",
            "productFamily" : "ethernet"
        }
        api_url = self.url + self.address_url + "?postcode=" + postcode + "&streetNr=10"
        print(api_url)
        response = requests.get(api_url, headers=headers)
        return response

    def quote_api(self, body):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.token,
            "APIGW-Tracking-Header": "96bb97fa-b941-46bb-8c4e-86c616c28a15"
        }
        api_url = self.url + self.quote_url
        response = requests.post(api_url, headers=headers, json = body)
        return response
    #add a decision to check if accessTypes is Fibre or FTTC.
    def get_quote(self, postcode, filters):
        #iterate through bandwidths, map to BTW value and add a new quoteItem to JSON
        quote_list = {"quoteItem": []}
        print(filters)
        print(filters["accessTypes"])
        if not filters["accessTypes"]:
            quote_list = add_quote_item(quote_list, filters, '100 Mbit/s', "EtherwayFibreService")
            print(quote_list)
            quote_list = add_quote_item(quote_list, filters, '1 Gbit/s', "EtherwayFibreService")
            quote_list = add_quote_item(quote_list, filters, '10 Gbit/s', "EtherwayFibreService")
            quote_list = add_quote_item(quote_list, filters, 'FTTC 40:10 Mbit/s', "EtherwayGEAService")
            print(quote_list)
            quote_list = add_quote_item(quote_list, filters, 'FTTC 80:20 Mbit/s', "EtherwayGEAService")
        else:
            for type in filters["accessTypes"]:
                if type == "Fibre":
                    product = "EtherwayFibreService"
                    if not filters["bearers"]:
                        quote_list = add_quote_item(quote_list, filters, '100 Mbit/s', product)
                        quote_list = add_quote_item(quote_list, filters, '1 Gbit/s', product)
                        quote_list = add_quote_item(quote_list, filters, '10 Gbit/s', product)
                    else:
                        for bearer in filters["bearers"]:
                            if bearer == 'BEARER_100':
                                bw = '100 Mbit/s'
                                quote_list = add_quote_item(quote_list, filters, bw, product)
                            elif bearer == 'BEARER_1000':
                                bw = '1 Gbit/s'
                                quote_list = add_quote_item(quote_list, filters, bw, product)
                            elif bearer == 'BEARER_10000':
                                bw = '10 Gbit/s'
                                quote_list = add_quote_item(quote_list, filters, bw, product)
                elif type == "FTTC":
                    product = "EtherwayGEAService"
                    if not filters["bearers"]:
                        quote_list = add_quote_item(quote_list, filters, 'FTTC 40:10 Mbit/s', product)
                        quote_list = add_quote_item(quote_list, filters, 'FTTC 80:20 Mbit/s', product)
                    else:
                        for bearer in filters["bearers"]:
                            if bearer == 'BEARER_100':
                                bw = 'FTTC 40:10 Mbit/s'
                                quote_list = add_quote_item(quote_list, filters, bw, product)
                                bw = 'FTTC 80:20 Mbit/s'
                                quote_list = add_quote_item(quote_list, filters, bw, product)
        response = self.quote_api(quote_list)
        return response

    # Cleanse NewOrder form.
    def create_order(self, filter):
        body = btw_order_api_body(filter)
        print(body)
        response = self.send_order(body)
        return response

    # Send cleansed order to 3rd Party order API.
    def send_order(self, body):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.token,
            "APIGW-Tracking-Header": "96bb97fa-b941-46bb-8c4e-86c616c28a15",
            "productFamily" : "ethernet"
        }
        api_url = self.url + self.order_url
        print(api_url)
        response = requests.post(api_url, headers=headers, json = body)
        print(response)
        print(response.content)
        return response



v1_api =BasicProvider("Virtual 1", "https://apitest.virtual1.com/",
                  "layer2-api/quoting", "layer2-api/retrieveQuote?quoteReference=",
                  "layer2-api/orderingV2", "address-lookup", v1_user, v1_password)

btw_test_api = OAuthProvider("BT Wholesale", "https://api-testa.business.bt.com/tmf-api/quoteManagement/v4",
                        "/quote", "/quote", "no_address_mgmt", "no_qual", "no_order",
                        btw_client_id ,btw_secret , "https://api-testa.business.bt.com/oauth/accesstoken")

btw_sandbox_api = OAuthProvider(
    "BT Wholesale sandbox", "https://api-sandbox.wholesale.bt.com",
    "/quote", "/retrieveQuote","/common/geographicAddressManagement/v1/geographicAddress",
    "/bt-wholesale/v1/product-qualification/ethernet",
    "/v1/productOrderingManagement/productOrder", btw_sandbox_client_id, btw_sandbox_secret,
    "https://api.wholesale.bt.com/oauth/accesstoken?grant_type=client_credentials")

