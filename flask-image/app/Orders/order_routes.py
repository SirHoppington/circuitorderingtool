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

@order.route('/new_order/<string:ref>', methods = ['POST', 'GET'])
@login_required
def new_order(ref):
    prov = check_provider(ref)
    form = NewOrder()
    if request.method == "POST":
        if prov[0].provider == "Virtual 1":
            try:
                order_request = new_orders.run(form.data, prov[0].provider)
                print(order_request)
            except Exception as e:
                return (str(e))

            return render_template("order_confirmation.html", order_ref=order_request[0], provider=order_request[1])

        else:
            try:
                order_request = new_orders.run(form.data, prov[0].provider)
                print(order_request)
            except Exception as e:
                return (str(e))
            return render_template("order_confirmation_btw.html", form=form, provider=prov[0].provider)
    else:
        # update db query to return Quotation table postcode
        form.postcode.data = prov[2].postcode
        form.Telephone.data = prov[3].telephone
        form.FirstName.data = prov[3].name
        form.LastName.data = prov[3].lastName
        form.Email.data = prov[3].email
        if prov[0].provider == "Virtual 1":
            form.quoteReference.data = ref
            form.pricingRequestAccessProductId.data = prov[1].productReference
            form.pricingRequestHardwareId.data = prov[1].hardwareId
            form.nni.data = "V1C45349 - TestingDC"
            form.designType.data = "PBT Partner Connect Design"
            return render_template("place_order.html", form=form, net=ref)

        else:
            form.btwProductId.data = prov[0].quoteReference
            return render_template("place_order_btw.html", form=form, net=ref)


