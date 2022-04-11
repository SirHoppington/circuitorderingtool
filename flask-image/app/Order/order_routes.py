from flask import Blueprint, request, render_template
from app.forms import RetrieveQuote, NewOrder
from app.Order.order import new_order
from app.queries import get_all_orders

order = Blueprint('order', __name__, template_folder='templates')

@order.route('/view_orders', methods = ['GET'])
def view_orders():
    form = RetrieveQuote()
    # DB query to show orders that have been placed.
    orders = get_all_orders()
    if request.method == 'POST':
        return render_template("new_order.html", orders=orders)
    else:
        return render_template("view_orders.html", orders=orders, form=form)

@order.route('/place_order', methods = ['POST', 'GET'])
def place_order():
    form = NewOrder()
    if request.method == 'POST':
        order_request = new_order.run(form.data)
        return render_template("order_confirmation.html", html_table=order_request[0], quote_ref=order_request[1])
    else:
        return render_template("place_order.html", form=form)

@order.route('/new_order/<int:id>', methods = ['GET'])
def new_order():
    order_id = new_order.place(id)
    return render_template("new_order.html", net_ref=order_id)