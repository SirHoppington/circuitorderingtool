from flask import Blueprint, request, render_template
from app.forms import RetrieveQuote, NewOrder
from app.Orders.orders import new_orders
from app.queries import get_all_orders, check_provider
from flask_login import login_required, current_user

order = Blueprint('order', __name__, template_folder='templates')

@order.route('/view_orders', methods = ['GET'])
@login_required
def view_orders():
    form = RetrieveQuote()
    # DB query to show orders that have been placed.
    orders = get_all_orders()
    if request.method == 'POST':
        return render_template("new_order.html", orders=orders)
    else:
        return render_template("view_orders.html", orders=orders, form=form)

@order.route('/place_order', methods = ['POST', 'GET'])
@login_required
def place_order():
    form = NewOrder()
    if request.method == 'POST':
        try:
            order_request = new_orders.run(form.data)
        except Exception as e:
            return (str(e))
        #return render_template("order_confirmation.html", html_table=order_request[0], quote_ref=order_request[1])
        #return render_template( html_table=order_request)
        return "success"

    else:
        return render_template("place_order.html", form=form)

@order.route('/new_order/<string:ref>', methods = ['GET'])
@login_required
def new_order(ref):
    prov = check_provider(ref)
    form = NewOrder()
    if prov[0].provider == "Virtual 1":
        form.quoteReference.data = ref
        form.pricingRequestAccessProductId.data = prov[1].productReference
        print(prov[1].hardwareId)
        form.pricingRequestHardwareId.data = prov[1].hardwareId
        return render_template("place_order.html", form=form)

    else:
        return render_template("place_order_btw.html", form=form)

