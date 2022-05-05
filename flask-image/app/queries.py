from app.Models.association_table import ProviderQuote, NetRef, Quotation, Order, ProviderProduct, Customer
from app import db
import pandas as pd

"""DB queries"""

# search Provider table via Quote reference:
def search_provider(reference):
    result = db.session.query(ProviderQuote).filter(
        (quote_table.c.quotation_net == reference) & (quote_table.c.provider_id == ProviderQuote.id) & (
                ProviderQuote.provider == "Virtual1")).first()
    return result

# search Quotation table via Quote reference:
def search_quotation_ref(reference):
    result = db.session.query(Quotation).filter(
            (NetRef.quotation_net == Quotation.net) & (NetRef.provider_id == ProviderQuote.id) & (NetRef.order_id == Order.id) & (
                    Quotation.net == reference)).first()
    return result

#Search ProviderQuote and Quotation table for all results
def get_all_pricing():
    result = db.session.query(Quotation, ProviderQuote).filter(
        (NetRef.quotation_net == Quotation.net) & (NetRef.provider_id == ProviderQuote.id)).all()
    return result

#Search ProviderQuote and Quotation table for all results
def get_net_ref(ref):
    result = db.session.query(Quotation).filter(
        (NetRef.provider_id == ProviderQuote.id) & (NetRef.quotation_net == ref )).first()
    return result

#Search ProviderQuote and ProviderProduct table for all results
def get_provider_pricing(ref):
    result = db.session.query(ProviderQuote, ProviderProduct).filter(
        (NetRef.product_id == ProviderProduct.id) & (NetRef.provider_id == ProviderQuote.id) & (NetRef.quotation_net == ref)).all()
    return result

#Search ProviderQuote, Quotation and order table for all results
def get_all_orders():
    result = db.session.query(ProviderQuote, Quotation, Order).filter(
        (NetRef.quotation_net == Quotation.net) & (NetRef.provider_id == ProviderQuote.id)& (NetRef.order_id == Order.id)).all()
    return result

#Search ProviderQuote and Quotation table for v1 pricing
def search_v1_quote_by_id(reference):
    result = db.session.query(ProviderQuote).filter(
        (NetRef.quotation_net == reference) & (NetRef.provider_id == ProviderQuote.id)  & (Quotation.id == reference)).first()
    return result

#Search ProviderQuote and Quotation table for v1 pricing
def search_provider_pricing(reference):
    result = db.session.query(ProviderQuote).filter(
        (ProviderQuote.quoteReference == reference)).first()
    return result

def search_provider_products(reference):
    result = db.session.query(ProviderProduct).filter(
        (ProviderProduct.productReference == reference)).first()
    return result
def search_customer(email):
    result = db.session.query(Customer).filter(
        (Customer.email == email)).first()
    return result


def add_quote(panda, supplier_ref, postcode, reference, status, name, email):
    try:
        panda[0].to_sql(name='provider_product', con=db.engine, index=False, if_exists='append', method='multi')
        panda[1].to_sql(name='provider_pricing', con=db.engine, index=False, if_exists='append', method='multi')
    ## INSERT API-2 db.session.add and append quotes.
        new_quote = Quotation(name=postcode, net=reference)
        db.session.add(new_quote)
        new_order = Order(status=status)
        db.session.add(new_order)
        existing_customer = search_customer(email)
        if not existing_customer:
            existing_customer = Customer(name=name, email=email)
            db.session.add(existing_customer)
        db.session.commit()
        v1_quote = search_provider_pricing(supplier_ref)
        #v1_provider_pricing = search_provider_products(supplier_ref)
        products = panda[0]
        #print (products['productReference'].iloc[0])
        for x in products['productReference']:
            v1_pricing = search_provider_products(x)
            associate_network_ref = NetRef(provider=v1_quote, product=v1_pricing, quotation=new_quote, order=new_order, customer=existing_customer)
            db.session.add(associate_network_ref)
            db.session.commit()
    except Exception as e:
        print (str(e))
    return new_quote

