from flask import request, json
import requests
import json
import pandas as pd


class Provider:
    def __init__(self, url):
        self.url = url


class Virtual1Api(Provider):
    headers = {
        "Content-Type": "application/json"
    }

    basic = requests.auth.HTTPBasicAuth('apiuser@capita.co.uk', 'EyNoe*Vr')

    v1_quote_mapper = {"accessType": "Access Type", "availableWithoutHardware": "Available without hardware",
                       "bandwidth": "Bandwidth(Mb)", "bearer": "Bearer(Mb)",
                       "carrier": "Carrier", "hardwareOptions": "Hardware", "indicative": "Indicative",
                       "installCharges": "Install Charges (GDP)",
                       "leadTime": "Lead Time (Days)", "monthlyFees": "Monthly fee (GDP)", "product": "Product",
                       "productReference": "Product ref", "secondaryOptions": "Secondary", "term": "Term",
                       "quoteReference": "Supplier Reference"}

    def get_quote(self, postcode, filters):
        quote_url = f"{self.url}layer2-api/quoting"
        cleansed_form = {k: v for k, v in filters.items() if v != ['Any'] and k != 'csrf_token' and k != 'postcode'}
        body = {"postcode":postcode, "filter":cleansed_form}
        response = requests.post(quote_url, headers=self.headers, data=json.dumps(body), auth=self.basic, verify=False)
        panda_pricing = pd.json_normalize(response.json(), record_path = ['accessProducts'], meta = ['quoteReference']).rename(columns=self.v1_quote_mapper)
        return panda_pricing

    def fetch_quote(self, quote_reference):
        retrieve_url = f"{self.url}layer2-api/retrieveQuote?quoteReference={quote_reference}"
        response = requests.get(retrieve_url)
        quote_details = pd.json_normalize(response.json(), record_path = ['accessProducts'], meta = ['quoteReference']).rename(columns=self.v1_quote_mapper)
        return quote_details

v1_api = Virtual1Api("https://apitest.virtual1.com/")







                