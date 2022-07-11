import pandas as pd

## Maps V1 JSON response to relevant panda columns
def map_v1_quote():
    result = {"accessType": "Access Type", "bandwidth": "Bandwidth(Mb)", "bearer": "Bearer(Mb)",
              "carrier": "Carrier", "installCharges": "Install Charges (GDP)",
              "leadTime": "Lead Time (Days)", "monthlyFees": "Monthly fee (GDP)", "product": "Product",
              "productReference": "Product ref", "term": "Term", "quoteReference": "Supplier Reference"}
    return result



## Convert API JSON response to Panda DataFrame:

def json_to_panda_v1(response):
    # v1_quote_map = map_v1_quote()
    #result = pd.json_normalize(response.json(), record_path=['accessProducts'],
    #                          meta=['quoteReference'])
    product_result = pd.json_normalize(response.json(), record_path=['accessProducts'])
    product_result.drop(['leadTime', 'availableWithoutHardware', 'hardwareOptions', 'secondaryOptions', 'indicative'], axis=1,
                inplace=True)
    product_result["customer_quote"] = "none"
    quote_result = pd.json_normalize(response.json(), meta=['quoteReference'])
    quote_result.drop(['accessProducts', 'hardwareProducts', 'secondaryAccess'], axis=1, inplace=True)
    print(quote_result)
    quote_result["provider"] = "Virtual 1"
    return product_result, quote_result

def add_quote_item(existing_list, postcode, bw):
    new_item = btw_api_body(postcode,bw)
    existing_list["quoteItem"].append(new_item)
    return existing_list

def btw_api_body(postcode,bandwidth):
    body = {"action": "add", "product": {"@type": "WholesaleEthernetElan",
                                                                    "productSpecification": {
                                                                        "id": "WholesaleEthernetElan"},
                                                                    "existingAend": "True",
                                                                    "place": [{"@type": "PostcodeSite",
                                                                               "postcode": postcode}], "product": [
                        {"@type": "EtherwayFibreService", "productSpecification":
                            {"id": "EtherwayFibreService"}, "bandwidth": bandwidth , "resilience": "Standard"},
                        {"@type": "EtherflowDynamicService",
                         "productSpecification": {"id": "EtherflowDynamicService"}, "bandwidth": "0.2 Mbit/s",
                         "cos": "Default CoS (Standard)"}]}}
    return body

def btw_api_body_fttc(postcode, bandwidth):
    body = {"quoteItem": [{"action": "add", "product": {"@type": "WholesaleEthernetElan",
                                                                    "productSpecification": {
                                                                        "id": "WholesaleEthernetElan"},
                                                                    "existingAend": "True",
                                                                    "place": [{"@type": "PostcodeSite",
                                                                               "postcode": postcode}], "product": [
                        {"@type": "EtherwayGEAService", "productSpecification":
                            {"id": "EtherwayGEAService"}, "bandwidth": bandwidth , "resilience": "Standard"},
                        {"@type": "EtherflowDynamicService",
                         "productSpecification": {"id": "EtherflowDynamicService"}, "bandwidth": "0.2 Mbit/s",
                         "cos": "Default CoS (Standard)"}]}}]}