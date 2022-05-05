from flask import Blueprint, request, render_template
from app.forms import RetrieveQuote
from app.Quote.quote import pricing, fetch_pricing
from app.queries import search_quotation_ref, get_all_pricing, get_provider_pricing, get_net_ref

provider_pricing = Blueprint('provider_pricing', __name__, template_folder='templates')

@provider_pricing.route('/view_pricing', methods = ['POST', 'GET'])
def view_pricing():
    form = RetrieveQuote()
    if request.method == 'POST':
        net_ref = search_quotation_ref(form.net.data)
        fetch_quote = fetch_pricing.run(net_ref.id)
        return render_template("view_provider_pricing.html", pricing=pricing, net_ref=fetch_quote[1])
    else:
        quotes = get_all_pricing()
        return render_template("view_pricing.html", form=form, quotes=quotes)

@provider_pricing.route('/view_pricing/<int:net>', methods = ['GET'])
def get_pricing(net):
    pricing = get_provider_pricing(net)
    return render_template("view_provider_pricing.html", pricing=pricing, net_ref=net)