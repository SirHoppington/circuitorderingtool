from app.api.provider import v1_api, btw_test_api
import pandas as pd
from app.queries import search_v1_quote_by_id, add_v1_quote, add_btw_quote, add_customer


# Use case class to request a new quotation.
class NewQuote:
    def __init__(self):
        pass

    def run(self, postcode,bandwidths, filters, reference, name, email):

        # try V1 API:
        new_quote = add_customer( postcode, reference, "Not ordered", name, email)
        if ("TalkTalk Business" in filters["suppliers"]) or ("Virtual1" in filters["suppliers"]):
        #for providers in filters:
        #    if
            try:
                # returns v1 response as a Panda Dataframe with correct column headers.
                v1_response = v1_api.get_quote(postcode, filters)
                v1_quote = v1_response[1]
                v1_quote_ref = v1_quote['quoteReference'].iloc[0]
                add_v1_quote(v1_response, v1_quote_ref, new_quote[0], new_quote[1], new_quote[2])
            except Exception as e:
                return (str(e))
        ## Add try/except for future provider Quotation APIs.
        if "BT Wholesale" in filters["suppliers"]:
            try:
                btw_response = btw_test_api.get_quote(postcode, bandwidths, filters)
                if btw_response.content["code"] == "41:":
                    btw_test_api.fetch_access_token()
                    btw_response = btw_test_api.get_quote(postcode, filters)
                    add_btw_quote(btw_response, new_quote[0], new_quote[1], new_quote[2])
            except Exception:
                btw_test_api.fetch_access_token()
                btw_response = btw_test_api.get_quote(postcode, bandwidths, filters)
                add_btw_quote(btw_response, new_quote[0], new_quote[1], new_quote[2])
        try:
            net_ref = new_quote[0].net
            return net_ref
        except Exception as e:
            return (str(e))

# Use case class to retrieve a quote based on reference.
class FetchQuote:

    def __init__(self):
        pass

    def run(self, reference):
        try:
            net_ref = search_v1_quote_by_id(reference)
            print(net_ref)
        except Exception as e:
            return (str(e))
        v1_response = v1_api.fetch_quote(net_ref.quoteReference)
        return v1_response.to_html(classes=["table"], border="0", index=False), net_ref[1].net

pricing = NewQuote()
fetch_pricing = FetchQuote()