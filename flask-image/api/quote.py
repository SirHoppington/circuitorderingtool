from api.virtual1 import v1_api
import pandas as pd
#from Provider.provider_model import ProviderQuote
#from Quote.quote_model import Quotation
#from Quote.association_table import quote_table
from Quote.association_table import NetRef, ProviderQuote, Quotation, Order
from app import db

class Quote():
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

            v1_ref = v1_response['Supplier Reference'].iloc[0]
            # Save to DB:
            v1_pricing = ProviderQuote(provider="Virtual1", supplier_ref=v1_ref)
            ## INSERT API-2 db.session.add and append to quotes.
            db.session.add(v1_pricing)
            new_quote = Quotation(name=postcode, net=reference)
            db.session.add(new_quote)
            new_order = Order(status="Not ordered")
            db.session.add(new_order)
            db.session.commit()
            associate_network_ref = NetRef(provider=v1_pricing, quote=new_quote, order=new_order)
            db.session.add(associate_network_ref)
            print(associate_network_ref)
            db.session.commit()
            net_ref = new_quote.net
            # Insert code to merge supplier pandas then return the results as html table.
            return v1_response.to_html(classes=["table"], border="0", index=False), net_ref
        except Exception as e:
            return (str(e))


    def retrieve_quote(self, reference):
        try:
            #v1_ref = db.session.query(ProviderQuote).filter((quote_table.c.quotation_id==Quotation.id) & (quote_table.c.provider_id==ProviderQuote.id) & (ProviderQuote.provider=="Virtual1") & (Quotation.net==reference)).first()
            v1_ref = db.session.query(ProviderQuote).filter((quote_table.c.quotation_id==reference) & (quote_table.c.provider_id==ProviderQuote.id) & (ProviderQuote.provider=="Virtual1")).first()
            net_ref = db.session.query(Quotation).filter((quote_table.c.quotation_id==reference) & (quote_table.c.provider_id==ProviderQuote.id) & (Quotation.id == reference)).first()
        except Exception as e:
            return (str(e))
        v1_response = v1_api.fetch_quote(v1_ref.supplier_ref)
        #net_ref = v1_ref.quotes.net
        return v1_response.to_html(classes=["table"], border="0", index=False), net_ref.net

pricing = Quote()