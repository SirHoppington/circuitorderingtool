from flask import Blueprint, request, render_template

callback = Blueprint('callback', __name__, template_folder='templates')

@callback.route('/productOrderCreateEvent', methods = ['POST', 'GET'])
def product_order_create_event():
    # Recieve order confirmation callback..
    if request.method == 'POST':
        order_ref = request.json['eventId']
        # add "order_ref" to database similar to v1 function below:
        #def add_v1_order(response, product):
        #    dict = response.json()
        #    order_ref = dict["resultOrderNumber"]
        #    set_order_ref(product, order_ref)
        #    return order_ref, "Virtual 1"
