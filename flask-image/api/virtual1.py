from flask import request, json
import requests

url = 'https://apitest.virtual1.com'
 
 
class Virtual1Api:

    def __init__(self):
        pass

    def get_quote(self, postcode):
        #for arg in kwargs:
         #   if arg == suppliers:
        body = { "postcode": postcode }
        #quoting = f"{url}/layer2-api/quoting"
        quoting = "https://apitest.virtual1.com/layer2-api/quoting"
        headers = {
            "Content-Type": "application/json"
        }
        basic = requests.auth.HTTPBasicAuth('apiuser@capita.co.uk', 'EyNoe*Vr')
        response = requests.post(quoting, headers=headers, json=body, auth=basic, verify=False)
        return response.json()






                