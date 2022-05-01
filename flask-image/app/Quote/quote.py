from app.api.provider import v1_api
import pandas as pd
from app.queries import search_v1_quote_by_id, add_quote


# Use case class to request a new quotation.
class NewQuote:
    def __init__(self):
        pass

    def run(self, postcode, filters, reference):

        # try V1 API:
        try:
            # returns v1 response as a Panda Dataframe with correct column headers.
            v1_response = v1_api.get_quote(postcode, filters)
        except Exception as e:
            return (str(e))
        ## Add try/except for future provider Quotation APIs.
        try:
            v1_quote = v1_response[1]
            v1_quote_ref = v1_quote['quoteReference'].iloc[0]
            ## Add quote to Database
            new_quote = add_quote(v1_response, v1_quote_ref, postcode, reference, "Not ordered")
            print("test")
            net_ref = new_quote.net
            # Insert code to merge supplier pandas then return the results as html table.
            return v1_response[0].to_html(classes=["table"], border="0", index=False), net_ref
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