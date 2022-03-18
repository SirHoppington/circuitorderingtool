from api.virtual1 import v1_api
import pandas as pd
from Provider.provider_model import ProviderQuote
from Quote.quote_model import Quotation
from Quote.association_table import quote_table
from app import db

class Quote():
    def __init__(self):
        pass

    def run(self, postcode, filters):
        #returns v1 response as a Panda Dataframe with correct column headers.
        v1_response = v1_api.get_quote(postcode, filters)

        # Insert code to merge supplier pandas then return the results as html table.
        supplier_ref = v1_response['Supplier Reference'].iloc[0]
        try:
            new_pricing = ProviderQuote(provider="Virtual1", supplier_ref=supplier_ref)
            new_quote = Quotation(name=postcode)
            db.session.add(new_pricing)
            new_pricing.quotes.append(new_quote)
            db.session.commit()
            quote_id = new_quote.id
            return v1_response.to_html(classes=["table"], border="0", index=False), quote_id
        except Exception as e:
            return(str(e))

    def retrieve_quote(self, reference):
        v1_ref = db.session.query(ProviderQuote).filter((quote_table.c.quotation_id==reference) & (quote_table.c.provider_id==ProviderQuote.id)).first()
        v1_response = v1_api.fetch_quote(v1_ref.supplier_ref)
        return v1_response.to_html(classes=["table"], border="0", index=False), reference


pricing = Quote()