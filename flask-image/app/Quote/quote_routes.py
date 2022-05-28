from flask import Blueprint, request, render_template
from app.forms import NewQuote, RetrieveQuote
from app.Quote.quote import pricing, fetch_pricing
from app.queries import search_quotation_ref, get_all_pricing, get_provider_pricing, get_net_ref, search_products_ref, add_product_to_quote, get_quotation_products

customer_quote = Blueprint('customer_quote', __name__, template_folder='templates')

@customer_quote.route('/new_quote', methods = ['POST', 'GET'])
def new_quote():
    form = NewQuote()
    if request.method == 'POST':
        quote_request = pricing.run(form.postcode.data, form.data, form.net.data, form.customer_name.data, form.customer_email.data)
        supplier_pricing = get_provider_pricing(quote_request)
        return render_template("view_provider_pricing.html",pricing=supplier_pricing, net_ref=quote_request)
    else:
        return render_template("new_quote.html", form=form)

@customer_quote.route('/add_quote/<int:net>', methods = ['POST'])
def add_quote(net):
    product_refs = request.form.getlist("prod_ref")
    print(product_refs)
    for product in product_refs:
        add_product_to_quote(product)
    #return render_template("view_provider_pricing.html",pricing=supplier_pricing, net_ref=quote_request)
    return "products added to quote!"
    #return render_template("view_provider_pricing.html",pricing=supplier_pricing, net_ref=quote_request)

@customer_quote.route('/', methods = ['POST', 'GET'])
@customer_quote.route('/view_quotations', methods = ['POST', 'GET'])
def view_quotations():
    form = RetrieveQuote()
    if request.method == 'POST':
        net_ref = search_quotation_ref(form.net.data)
        fetch_quote = fetch_pricing.run(net_ref.id)
        return render_template("view_quotation.html", pricing=pricing, net_ref=fetch_quote[1])
    else:
        quotes = get_all_pricing()
        return render_template("view_all_quotations.html", form=form, quotes=quotes)

@customer_quote.route('/view_quotation/<int:net>', methods = ['GET'])
def get_quotation(net):
    pricing = get_provider_pricing(net)
    quote = get_quotation_products(net)
    return render_template("view_quotation.html", pricing=quote, net_ref=net)