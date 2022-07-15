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

# search ProviderProduct table via product reference:
def search_products_ref(ref):
    result = db.session.query(ProviderProduct).filter(
            (ProviderProduct.id == ref)).first()
    return result

def search_net_order(ref):
    result = db.session.query(Order).filter(
            (Quotation.net == ref) & (NetRef.order_id == Order.id) & (NetRef.quotation_net == ref)).first()
    return result
def search_prod_order(product):
    result = db.session.query(Order).filter(
            (NetRef.order_id == Order.id) & (NetRef.product_id == ProviderProduct.id) & (ProviderProduct.productReference == product)).first()
    return result


#Search ProviderQuote and Quotation table for all results
def get_all_pricing():
    result = db.session.query(Quotation, ProviderQuote, Customer).filter(
        (NetRef.quotation_net == Quotation.net) & (NetRef.provider_id == ProviderQuote.id) & (NetRef.customer_id == Customer.id)).all()
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
def get_quotation_products(ref):
    result = db.session.query(ProviderQuote, ProviderProduct).filter(
        (NetRef.product_id == ProviderProduct.id) & (NetRef.provider_id == ProviderQuote.id) & (NetRef.quotation_net == ref) & (ProviderProduct.customer_quote == "Added")).all()
    return result

#Search ProviderQuote, Quotation and order table for all results
def get_all_orders():
    result = db.session.query(ProviderQuote, Quotation, Order).filter(
        (NetRef.quotation_net == Quotation.net) & (NetRef.provider_id == ProviderQuote.id)& (NetRef.order_id == Order.id) & (Order.status != "Not ordered")).all()
    print(result)
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

def add_customer(postcode, reference, status, name, email):
    new_quote = Quotation(name=postcode, net=reference)
    db.session.add(new_quote)
    new_order = Order(status=status, ref=None)
    db.session.add(new_order)
    existing_customer = search_customer(email)
    if not existing_customer:
        existing_customer = Customer(name=name, email=email)
        db.session.add(existing_customer)
    db.session.commit()
    return new_quote, new_order, existing_customer

def add_v1_order(response, product):
    dict = response.json()
    order_ref = dict["resultOrderNumber"]
    set_order_ref(product, order_ref)
    return order_ref, "Virtual 1"


def add_v1_quote(response,new_quote, new_order, existing_customer):
    dict = response.json()
    v1_ref = dict["quoteReference"]
    v1_quote = ProviderQuote(quoteReference=v1_ref, provider="Virtual 1")
    db.session.add(v1_quote)
    db.session.commit()
    print(dict["accessProducts"])
    for item in dict["accessProducts"]:
        product_ref = item["productReference"]
        access = item["accessType"]
        if item["accessType"] == "Copper":
            bearer = " "
            bandwidth = " "
        else:
            bearer = item["bearer"]
            bandwidth = item["bandwidth"]
        carrier = item["carrier"]
        product = item["product"]
        term = item["term"]
        access_prod = item["productReference"]
        hardware = item["hardwareOptions"][0]["hardwareReference"]
        install = item["installCharges"]
        monthly = item["monthlyFees"]
        new_product = ProviderProduct(accessType=access, bandwidth=bandwidth, bearer=bearer, carrier=carrier,
                                      installCharges=install, monthlyFees=monthly, product=product, productReference=access_prod, hardwareId=hardware, term=term, customer_quote="none")
        db.session.add(new_product)
        associate_network_ref = NetRef(provider=v1_quote,product=new_product, quotation=new_quote, order=new_order, customer=existing_customer)
        db.session.add(associate_network_ref)
        db.session.commit()
    return True

def add_btw_quote(response,new_quote, new_order, existing_customer):
    dict = response.json()
    print(dict)
    bt_ref = dict["id"]
    print(bt_ref)
    btw_quote = ProviderQuote(quoteReference=bt_ref, provider="BT Wholesale")
    db.session.add(btw_quote)
    db.session.commit()
    for item in dict["quoteItem"]:
        if "errors" in item["product"]["product"][1]:
            print(item["product"]["product"][1]["errors"])
        else:
            access = item["product"]["product"][0]["@type"]
            bearer = item["product"]["product"][0]["bandwidth"]
            bandwidth = item["product"]["product"][1]["bandwidth"]
            carrier = item["product"]["product"][0]["productInformation"]["accessProvider"]
            product = item["product"]["@type"]
            counter = 0
            nr_charges = []
            r_charges = []
            terms = []
            for x, y in zip(item["product"]["product"][0] ["productPrice"], item["product"]["product"][1] ["productPrice"]):
                if (counter % 2) ==0:
                    nr_charges.append(x["price"]["taxIncludedAmount"]["value"] + y["price"]["taxIncludedAmount"]["value"])
                    terms.append(x["name"])
                else:
                    r_charges.append(x["price"]["taxIncludedAmount"]["value"] + y["price"]["taxIncludedAmount"]["value"])
                counter += 1
            for a, b, c in zip(nr_charges, r_charges, terms):
                new_product = ProviderProduct(accessType=access, bandwidth=bandwidth, bearer=bearer, carrier=carrier,
                                      installCharges=a, monthlyFees=b, product=product, productReference="NA",hardwareId="NA", term= c, customer_quote="none")
                db.session.add(new_product)
                associate_network_ref = NetRef(provider=btw_quote,product=new_product, quotation=new_quote, order=new_order, customer=existing_customer)
                db.session.add(associate_network_ref)
                db.session.commit()
    return True

def add_product_to_quote(product):
    prod = search_products_ref(product)
    prod.customer_quote = "Added"
    db.session.commit()
    return True

def remove_product_from_quote(product):
    prod = search_products_ref(product)
    prod.customer_quote = "none"
    db.session.commit()
    return True

def send_quote_to_order(product):
    order = search_net_order(product)
    order.status = "Orders requested"
    db.session.commit()
    return True

def set_order_ref(product, order_ref):
    order = search_prod_order(product)
    order.ref = order_ref
    order.status = "Order sent"
    db.session.commit()
    return True

# check if it is a virtual1 quote:
def check_provider(ref):
    result = db.session.query(ProviderQuote, ProviderProduct).filter(
        (ProviderQuote.quoteReference == ref) & (NetRef.provider_id == ProviderQuote.id) & (NetRef.product_id == ProviderProduct.id)).first()
    return result
