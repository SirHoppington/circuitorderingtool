import os
from flask import Blueprint, request, jsonify, make_response, render_template, render_template_string, url_for, redirect, json
from forms import NewQuote
from api.quote import pricing
import pandas as pd
import json
import pandas as pd

provider = Blueprint('provider', __name__)

@provider.route('/new_quote', methods = ['POST', 'GET'])
def new_quote():
    form = NewQuote()
    if request.method == 'POST':
        quote_request = pricing.run(form.postcode.data, form.data)
        return render_template("panda_quote.html", html_table=quote_request)
    else:
        return render_template("new_quote.html", form=form)

@provider.route('/view_pricing', methods = ['POST', 'GET'])
def view_pricing():
    form = retrieveQuote()
    if request.method == 'POST':
        fetch_quote = pricing.retrieve_quote(form.quote_ref.data)
        return render_template(view_pricing_results.html, html_table=fetch_quote)
    else:
        return render_template("view_pricing.html", form=form)