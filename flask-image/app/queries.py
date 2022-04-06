from app.Models.association_table import ProviderQuote, NetRef, Quotation, Order
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

def add_quote(provider, supplier_ref, postcode, reference, status):
    v1_pricing = ProviderQuote(provider=provider, supplier_ref=supplier_ref)
    ## INSERT API-2 db.session.add and append to quotes.
    db.session.add(v1_pricing)
    new_quote = Quotation(name=postcode, net=reference)
    db.session.add(new_quote)
    new_order = Order(status=status)
    db.session.add(new_order)
    db.session.commit()
    associate_network_ref = NetRef(provider=v1_pricing, quote=new_quote, order=new_order)
    db.session.add(associate_network_ref)
    print(associate_network_ref)
    db.session.commit()
    return new_quote

