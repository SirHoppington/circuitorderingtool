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
    quote_result["provider"] = "Virtual 1"
    return product_result, quote_result
