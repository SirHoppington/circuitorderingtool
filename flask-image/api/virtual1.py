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

    v1_quote_mapper = {"accessType": "Access Type", "bandwidth": "Bandwidth(Mb)", "bearer": "Bearer(Mb)",
    "carrier": "Carrier", "installCharges": "Install Charges (GDP)",
    "leadTime": "Lead Time (Days)", "monthlyFees": "Monthly fee (GDP)", "product": "Product",
    "productReference": "Product ref", "term": "Term", "quoteReference": "Supplier Reference"}

    def get_quote(self, postcode, filters):
        quote_url = f"{self.url}layer2-api/quoting"
        cleansed_form = {k: v for k, v in filters.items() if v != ['Any'] and k != 'csrf_token' and k != 'postcode'}
        body = {"postcode":postcode, "filter":cleansed_form}
        response = requests.post(quote_url, headers=self.headers, data=json.dumps(body), auth=self.basic, verify=False)
        panda_pricing = pd.json_normalize(response.json(), record_path=['accessProducts'],
                                          meta=['quoteReference']).rename(columns=self.v1_quote_mapper)
        panda_pricing.drop(['availableWithoutHardware', 'hardwareOptions', 'secondaryOptions', 'indicative'], axis=1,
                           inplace=True)

        #will save all of panda to database table, likely best to only save quotation reference.
        #panda.to_sql(name='provider_pricing', con=db.engine, index=False)
        return panda_pricing

    def fetch_quote(self, quote_reference):
        retrieve_url = f"{self.url}layer2-api/retrieveQuote?quoteReference={quote_reference}"
        response = requests.get(retrieve_url, auth=self.basic)
        panda_pricing = pd.json_normalize(response.json(), record_path = ['accessProducts'], meta = ['quoteReference']).rename(columns=self.v1_quote_mapper)
        panda_pricing.drop(['availableWithoutHardware', 'hardwareOptions', 'secondaryOptions', 'indicative'], axis=1,
                           inplace=True)
        return panda_pricing

    def create_order(self, order_details):
        order_url = f"{self.url}layer2-api/ordering"
        response = requests.get(order_url, auth=self.basic)
        panda_pricing = pd.json_normalize(response.json(), record_path = ['accessProducts'], meta = ['quoteReference']).rename(columns=self.v1_quote_mapper)
        panda_pricing.drop(['availableWithoutHardware', 'hardwareOptions', 'secondaryOptions', 'indicative'], axis=1,
                           inplace=True)
        return panda_pricing


v1_api = Virtual1Api("https://apitest.virtual1.com/")







                