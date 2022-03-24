from flask import Blueprint, request, jsonify, make_response, render_template, render_template_string, url_for, redirect, json
from forms import NewQuote, RetrieveQuote, NewOrder
import pandas as pd
import json
from api.quote import pricing
from api.order import new_order
from Provider.provider_model import ProviderQuote
from Quote.quote_model import Quotation
from Quote.association_table import quote_table
from app import db

provider = Blueprint('provider', __name__)

@provider.route('/new_quote', methods = ['POST', 'GET'])
def new_quote():
    form = NewQuote()
    if request.method == 'POST':
        quote_request = pricing.run(form.postcode.data, form.data, form.net.data)
        return render_template("panda_quote.html", html_table=quote_request[0], net_ref=quote_request[1])
    else:
        return render_template("new_quote.html", form=form)

@provider.route('/view_pricing', methods = ['POST', 'GET'])
def view_pricing():
    form = RetrieveQuote()
    quotes = db.session.query(ProviderQuote).filter(
        (quote_table.c.quotation_id == Quotation.id) & (quote_table.c.provider_id == ProviderQuote.id)).all()
    if request.method == 'POST':
        net_ref = db.session.query(Quotation).filter(
            (quote_table.c.quotation_id == Quotation.id) & (quote_table.c.provider_id == ProviderQuote.id) & (
                    Quotation.net == form.net.data)).first()
        fetch_quote = pricing.retrieve_quote(net_ref.id)
        return render_template("panda_quote.html", html_table=fetch_quote[0], net_ref=fetch_quote[1])
    else:
        return render_template("view_pricing.html", form=form, quotes=quotes)

@provider.route('/view_orders', methods = ['GET'])
def view_orders():
    # DB query to show orders that have been placed.
    #quotes= db.session.query(ProviderQuote).filter((quote_table.c.quotation_id==Quotation.id) & (quote_table.c.provider_id==ProviderQuote.id)).all()
    return render_template("view_orders.html", quotes=quotes)

@provider.route('/place_order', methods = ['POST', 'GET'])
def place_order():
    form = NewOrder()
    if request.method == 'POST':
        order_request = new_order.run(form.data)
        return render_template("order_confirmation.html", html_table=order_request[0], quote_ref=order_request[1])
    else:
        return render_template("new_order.html", form=form)

@provider.route('/view_pricing/<int:id>', methods = ['GET'])
def get_pricing(id):
    fetch_quote = pricing.retrieve_quote(id)
    return render_template("panda_quote.html", html_table=fetch_quote[0], net_ref=fetch_quote[1])

#@provider.route('/view_order/<int:id>', methods = ['POST', 'GET'])
#def get_order(id):
#    fetch_quote = pricing.retrieve_quote(net)
#    return render_template("panda_quote.html", html_table=fetch_quote[0], net_ref=fetch_quote[1])