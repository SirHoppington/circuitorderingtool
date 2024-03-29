from app.api.provider import v1_api, btw_test_api
import pandas as pd
from app.queries import search_v1_quote_by_id, add_v1_quote, add_btw_quote, add_customer


# Use case class to request a new quotation.
class NewQuote:
    def __init__(self):
        pass

    def run(self, postcode, filters, reference, name, email, customer_lastName, customer_telephone):

        # try V1 API:
        new_quote = add_customer( postcode, reference, "Not ordered", name, email, customer_lastName, customer_telephone)
        print(filters)
        if not filters["suppliers"]:
            try:
                v1_response = v1_api.get_quote(postcode, filters)
                add_v1_quote(v1_response, new_quote[0], new_quote[1], new_quote[2])
            except Exception as e:
                return (str(e))
            try:
                if "Copper" not in filters["accessTypes"]:
                    btw_response = btw_test_api.get_quote(postcode, filters)
                    add_btw_quote(btw_response, new_quote[0], new_quote[1], new_quote[2])
            except:
                    btw_test_api.fetch_access_token()
                    btw_response = btw_test_api.get_quote(postcode, filters)
                    add_btw_quote(btw_response, new_quote[0], new_quote[1], new_quote[2])

        if ("TalkTalk Business" in filters["suppliers"]) or ("Virtual1" in filters["suppliers"]):
        #for providers in filters:
        #    if
            try:
                # returns v1 response as a Panda Dataframe with correct column headers.
                v1_response = v1_api.get_quote(postcode, filters)
                add_v1_quote(v1_response, new_quote[0], new_quote[1], new_quote[2])
            except Exception as e:
                return (str(e))

        if "BT Wholesale" in filters["suppliers"]:
            if ("Fibre" in filters["accessTypes"]) or \
                    ("FTTC" in filters["accessTypes"] or not filters["accessTypes"]):
                try:
                    btw_response = btw_test_api.get_quote(postcode, filters)
                    add_btw_quote(btw_response, new_quote[0], new_quote[1], new_quote[2])
                except:
                    btw_test_api.fetch_access_token()
                    btw_response = btw_test_api.get_quote(postcode, filters)
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