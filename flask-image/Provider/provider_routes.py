import os
from flask import Blueprint, request, jsonify, make_response, render_template, render_template_string, url_for, redirect, json
from forms import NewQuote, RetrieveQuote
from api.quote import pricing
import pandas as pd
import json
from Provider.provider_model import ProviderQuote
from Quote.quote_model import Quotation
from Quote.association_table import quote_table
from app import db

provider = Blueprint('provider', __name__)

@provider.route('/new_quote', methods = ['POST', 'GET'])
def new_quote():
    form = NewQuote()
    if request.method == 'POST':
        quote_request = pricing.run(form.postcode.data, form.data)
        return render_template("panda_quote.html", html_table=quote_request[0], quote_ref=quote_request[1])
    else:
        return render_template("new_quote.html", form=form)

@provider.route('/view_pricing', methods = ['POST', 'GET'])
def view_pricing():
    form = RetrieveQuote()
 #   if request.method == 'POST':
 #       fetch_quote = pricing.retrieve_quote(form.quote_ref.data)
 #       return render_template("panda_quote.html", html_table=fetch_quote[0], quote_ref=fetch_quote[1])
 #   else:
        # Move DB queries to separate module and import, keeps the views clean.
    quotes= db.session.query(ProviderQuote).filter((quote_table.c.quotation_id==Quotation.id) & (quote_table.c.provider_id==ProviderQuote.id)).all()
    return render_template("view_pricing.html", form=form, quotes=quotes)

@provider.route('/view_quotation_table', methods = ['POST', 'GET'])
def view_quotation_table():
        return render_template("view_quote_table.html")

@provider.route('/view_pricing/<int:id>', methods = ['GET'])
def get_pricing(id):
    fetch_quote = pricing.retrieve_quote(id)
    return render_template("panda_quote.html", html_table=fetch_quote[0], quote_ref=fetch_quote[1])
