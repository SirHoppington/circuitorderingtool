#from Provider.provider_model import ProviderQuote
#from Quote.quote_model import Quotation
#from Quote.association_table import quote_table
from Quote.association_table import ProviderQuote, NetRef, Quotation, Order
from app import db

"""DB queries"""

# search Provider table via Quote reference:
def search_provider(reference):
    result = db.session.query(ProviderQuote).filter(
        (quote_table.c.quotation_id == reference) & (quote_table.c.provider_id == ProviderQuote.id) & (
                ProviderQuote.provider == "Virtual1")).first()
    return result

# search Quotation table via Quote reference:
def search_quotation_ref(reference):
    result = db.session.query(Quotation).filter(
            (NetRef.quotation_id == Quotation.id) & (NetRef.provider_id == ProviderQuote.id) & (NetRef.order_id == Order.id) & (
                    Quotation.net == reference)).first()
    return result

#Search ProviderQuote and Quotation table for all results
def get_all_pricing():
    result = db.session.query(ProviderQuote, Quotation).filter(
        (NetRef.quotation_id == Quotation.id) & (NetRef.provider_id == ProviderQuote.id)& (NetRef.order_id == Order.id)).all()
    return result

#Search ProviderQuote and Quotation table for v1 pricing
def search_v1_quote_by_id(reference):
    result = db.session.query(ProviderQuote, Quotation).filter(
        (NetRef.quotation_id == reference) & (NetRef.provider_id == ProviderQuote.id) & (
                ProviderQuote.provider == "Virtual1") & (Quotation.id == reference)).first()
    return result