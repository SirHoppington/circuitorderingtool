from app.api.provider import v1_api, btw_test_api
import pandas as pd
from app.queries import search_v1_quote_by_id, add_v1_quote, add_btw_quote, add_customer

# Use case class to request a new quotation.


class NewOrder:
    def __init__(self):
        pass

    def run(self, filters):
        # try V1 API:
        try:
            # returns v1 response as a Panda Dataframe with correct column headers.
            v1_response = v1_api.create_order(filters)
        except Exception as e:
            return (str(e))
        ## Add try/except for future provider Quotation APIs.
        try:
            # Insert code to merge supplier pandas then return the results as html table.
            return v1_response
            #return v1_response.to_html(classes=["table"], border="0", index=False)
        except Exception as e:
            return (str(e))

#    def place(self, reference):
#        order = Order(status="Assigned")
#        db.session.add(order)
#        quote_ref = Quotation(name=postcode)
#        v1_pricing.quotes.append(new_quote)
#        db.session.add(new_quote)
#        db.session.commit()

new_orders = NewOrder()
        