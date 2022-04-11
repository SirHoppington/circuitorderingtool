from flask import Blueprint, request, render_template
from app.forms import NewQuote, RetrieveQuote
from app.Quote.quote import pricing, fetch_pricing
from app.queries import search_quotation_ref, get_all_pricing, search_v1_quote_by_id

provider_pricing = Blueprint('provider_pricing', __name__, template_folder='templates')

@provider_pricing.route('/new_quote', methods = ['POST', 'GET'])
def new_quote():
    form = NewQuote()
    if request.method == 'POST':
        quote_request = pricing.run(form.postcode.data, form.data, form.net.data)

        return render_template("panda_quote.html", html_table=quote_request[0], net_ref=quote_request[1])
    else:
        return render_template("new_quote.html", form=form)

@provider_pricing.route('/view_pricing', methods = ['POST', 'GET'])
def view_pricing():
    form = RetrieveQuote()
    if request.method == 'POST':
        net_ref = search_quotation_ref(form.net.data)
        fetch_quote = fetch_pricing.run(net_ref.id)
        return render_template("panda_quote.html", html_table=fetch_quote[0], net_ref=fetch_quote[1])
    else:
        quotes = get_all_pricing()
        return render_template("view_pricing.html", form=form, quotes=quotes)

@provider_pricing.route('/view_pricing/<int:id>', methods = ['GET'])
def get_pricing(id):
    fetch_quote = fetch_pricing.run(id)
    return render_template("panda_quote.html", html_table=fetch_quote[0], net_ref=fetch_quote[1])