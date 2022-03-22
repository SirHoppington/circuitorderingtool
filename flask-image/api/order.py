from api.virtual1 import v1_api
import pandas as pd
from Provider.provider_model import ProviderQuote
from Quote.quote_model import Quotation
from Quote.association_table import quote_table
from app import db

class Order():
    def __init__(self):
        pass

    def run(self, postcode, filters):

        # try V1 API:
        try:
            # returns v1 response as a Panda Dataframe with correct column headers.
            v1_response = v1_api.get_quote(postcode, filters)
        except Exception as e:
            return (str(e))
        ## Add try/except for future provider Quotation APIs.
        try:

            v1_ref = v1_response['Supplier Reference'].iloc[0]
            # Save to DB:
            v1_pricing = ProviderQuote(provider="Virtual1", supplier_ref=v1_ref)
            ## INSERT API-2 db.session.add and append to quotes.
            db.session.add(v1_pricing)
            new_quote = Quotation(name=postcode)
            v1_pricing.quotes.append(new_quote)
            db.session.add(new_quote)
            db.session.commit()
            quote_id = new_quote.id
            # Insert code to merge supplier pandas then return the results as html table.
            return v1_response.to_html(classes=["table"], border="0", index=False), quote_id
        except Exception as e:
            return (str(e))


    def retrieve_quote(self, reference):
        try:
            v1_ref = db.session.query(ProviderQuote).filter((quote_table.c.quotation_id==reference) & (quote_table.c.provider_id==ProviderQuote.id) & (ProviderQuote.provider=="Virtual1")).first()
        except Exception as e:
            return (str(e))
        v1_response = v1_api.fetch_quote(v1_ref.supplier_ref)
        return v1_response.to_html(classes=["table"], border="0", index=False), reference


new_order = Order()
        