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
    v1_quote_map = map_v1_quote()
    result = pd.json_normalize(response.json(), record_path=['accessProducts'],
                                      meta=['quoteReference']).rename(columns=v1_quote_map)
    result.drop(['availableWithoutHardware', 'hardwareOptions', 'secondaryOptions', 'indicative'], axis=1,
                       inplace=True)
    return result