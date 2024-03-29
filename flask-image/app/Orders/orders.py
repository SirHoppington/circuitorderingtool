from app.api.provider import v1_api, btw_test_api, btw_sandbox_api
import pandas as pd
from app.queries import search_v1_quote_by_id, add_v1_quote, add_btw_quote, add_customer, add_v1_order, set_btw_status

# Use case class to request a new quotation.
class NewOrder:
    def __init__(self):
        pass

    def run(self, filters, provider):
        # try V1 API:

        if provider == "Virtual 1":
            try:
                # returns v1 response as a Panda Dataframe with correct column headers.
                v1_response = v1_api.create_order(filters)
                order_ref = add_v1_order(v1_response, filters["pricingRequestAccessProductId"])
            except Exception as e:
                return (str(e))
        else:
            try:
                #manipulate form to gather required data
                btw_response = btw_sandbox_api.create_order(filters)
                # Change to set the btw order status
                order_ref = set_btw_status(filters["btwProductId"])
            except:
                btw_sandbox_api.fetch_access_token()
                btw_response = btw_sandbox_api.create_order(filters)
                order_ref = set_btw_status(filters["btwProductId"])

        ## Add try/except for future provider Quotation APIs.
        try:
                # Insert code to merge supplier pandas then return the results as html table.
            return order_ref
                #return v1_response.to_html(classes=["table"], border="0", index=False)
        except Exception as e:
            return (str(e))

new_orders = NewOrder()
        