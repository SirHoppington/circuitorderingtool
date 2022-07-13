
def add_quote_item(existing_list, filters, bw, product):
    new_item = btw_api_body(filters, bw, product)
    existing_list["quoteItem"].append(new_item)
    return existing_list

def btw_api_body(filters,bandwidth, product):

        body = {"action": "add", "product": {"@type": "WholesaleEthernetElan",
                                                                    "productSpecification": {
                                                                        "id": "WholesaleEthernetElan"},
                                                                    "existingAend": "True",
                                                                    "place": [{"@type": "PostcodeSite",
                                                                               "postcode": filters["postcode"]}], "product": [
                        {"@type": product, "productSpecification":
                            {"id": product}, "bandwidth": bandwidth , "resilience": "Standard"},
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