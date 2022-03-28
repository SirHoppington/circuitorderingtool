from Provider.provider_model import ProviderQuote
from Quote.quote_model import Quotation
from Quote.association_table import quote_table
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
    result = net_ref = db.session.query(Quotation).filter(
        (quote_table.c.quotation_id == reference) & (quote_table.c.provider_id == ProviderQuote.id) & (
                Quotation.id == reference)).first()
    return result

