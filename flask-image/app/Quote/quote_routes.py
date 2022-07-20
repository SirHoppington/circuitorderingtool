from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from app.forms import NewQuote, RetrieveQuote
from app.Quote.quote import pricing, fetch_pricing
from app.api.provider import btw_test_api, btw_sandbox_api
from app.api.provider import v1_api
from app.queries import search_quotation_ref, get_all_pricing, get_provider_pricing, \
    get_net_ref, search_products_ref, add_product_to_quote, get_quotation_products, \
    remove_product_from_quote, send_quote_to_order, get_all_orders

customer_quote = Blueprint('customer_quote', __name__, template_folder='templates')

@customer_quote.route('/new_quote', methods = ['POST', 'GET'])
@login_required
def new_quote():
    form = NewQuote()
    if request.method == 'POST':
        quote_request = pricing.run(form.postcode.data, form.data, form.net.data, form.customer_name.data, form.customer_email.data)
        supplier_pricing = get_provider_pricing(quote_request)
        if not supplier_pricing:
            return render_template("no_pricing_available.html")
        else:
            return render_template("view_provider_pricing.html",pricing=supplier_pricing, net_ref=quote_request)
    else:
        return render_template("new_quote.html", form=form)

# Postcode search, use AJAX to send to prevent form refresh
@customer_quote.route('/search_address', methods = ['POST', 'GET'])
def search_address():
    if request.method =='POST':
        postcode = request.json['postcode']
        try:
            result = btw_sandbox_api.address_lookup(postcode)
            if result.content["code"] == "41":
                btw_sandbox_api.fetch_access_token()
                result = btw_sandbox_api.address_lookup(postcode)
        except:
            btw_sandbox_api.fetch_access_token()
            result = btw_sandbox_api.address_lookup(postcode)
        print(result.content)
        return "yes"

@customer_quote.route('/test_quote', methods = ['POST', 'GET'])
@login_required
def test_quote():
    form = NewQuote()
    if request.method == 'POST':
        #quote_request = pricing.run(form.postcode.data, form.data, form.net.data, form.customer_name.data, form.customer_email.data)
        postcode = form.postcode.data
        try:
            v1_response = v1_api.get_quote(postcode, form.data)
            #btw_response = btw_test_api.get_quote(postcode, form.data)
            #if btw_response.content["code"]  == "41":
            #    btw_test_api.fetch_access_token()
            #    btw_response = btw_test_api.get_quote(postcode, form.data)
            print(v1_response.content)
        except Exception as e:
            return (str(e))
            #btw_test_api.fetch_access_token()
            #btw_response = btw_test_api.get_quote(postcode, form.data)
            #print(btw_response)
        #supplier_pricing = get_provider_pricing(quote_request)
        #return btw_response[0].to_html()
        return v1_response.content
        #return render_template("view_provider_pricing.html",pricing=supplier_pricing, net_ref=quote_request)
    else:
        return render_template("test_quote.html", form=form)


@customer_quote.route('/add_quote/<int:net>', methods = ['POST'])
@login_required
def add_quote(net):
    product_id = request.form.getlist("prod_id")
    print(product_id)
    for product in product_id:
        add_product_to_quote(product)
    quote = get_quotation_products(net)
    return render_template("view_quotation.html", pricing=quote, net_ref=net)

@customer_quote.route('/remove_quote/<int:net>', methods = ['POST'])
def remove_quote(net):
    product_id = request.form.getlist("prod_id")
    print(product_id)
    for product in product_id:
        remove_product_from_quote(product)
    quote = get_quotation_products(net)
    return render_template("view_quotation.html", pricing=quote, net_ref=net)

@customer_quote.route('/add_to_order/<int:net>', methods = ['POST'])
@login_required
def add_to_order(net):
    send_quote_to_order(net)
    form = RetrieveQuote()
    # DB query to show orders that have been placed.
    orders = get_all_orders()
    #return render_template("view_provider_pricing.html",pricing=supplier_pricing, net_ref=quote_request)
    return render_template("view_orders.html", orders=orders, form=form)

@customer_quote.route('/', methods = ['POST', 'GET'])
@customer_quote.route('/view_quotations', methods = ['POST', 'GET'])
@login_required
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
@login_required
def get_quotation(net):
    pricing = get_provider_pricing(net)
    quote = get_quotation_products(net)
    return render_template("view_quotation.html", pricing=quote, net_ref=net)