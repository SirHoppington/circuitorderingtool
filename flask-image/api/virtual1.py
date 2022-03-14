from flask import request, json
import requests
import json


class Provider:
    def __init__(self, url):
        self.url = url


class Virtual1Api(Provider):
    headers = {
        "Content-Type": "application/json"
    }

    basic = requests.auth.HTTPBasicAuth('apiuser@capita.co.uk', 'EyNoe*Vr')

    def get_quote(self, postcode, filters):
        # for arg in kwargs:
        #   if arg == suppliers:
        quoting = f"{self.url}layer2-api/quoting"
        #quoting = url
        #quoting = "https://apitest.virtual1.com/layer2-api/quoting"
        #body = {"postcode": postcode}
        body = {k: v for k, v in filters.items() if v != ['Any'] and k != 'csrf_token' and k != 'postcode'}
        full_body = {"postcode":postcode, "filter":body}
        json_data = json.dumps(full_body)
        #json_data = full_body
        response = requests.post(quoting, headers=self.headers, data=json_data, auth=self.basic, verify=False)
        return response.json()

v1_api = Virtual1Api("https://apitest.virtual1.com/")







                