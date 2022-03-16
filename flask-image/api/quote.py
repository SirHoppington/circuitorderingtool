from api.virtual1 import v1_api
import pandas as pd

class Quote():
    def __init__(self):
        pass

    def run(self, postcode, filters):
        #returns v1 response as a Panda Dataframe with correct column headers.
        v1_response = v1_api.get_quote(postcode, filters)

        # Insert code to merge supplier pandas then return the results as html table.

        return v1_response.to_html(classes=["table"], border="0", index=False)

    def retrieve_quote(self, reference):

        ## run DB search to retrieve v1 supplier reference:
        v1_response = v1.api.fetch_quote(reference)

        return v1_response


pricing = Quote()