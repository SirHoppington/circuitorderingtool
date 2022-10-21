from app.api.provider import v1_api
from app.Quote.quote import pricing
from app.queries import add_customer, add_v1_quote
from app.Models.association_table import Quotation, Order, Customer, ProviderQuote, ProviderProduct, NetRef
from app import db

#Integration test for V1 Provider API get_quote() function
def test_v1_quote(mock_post_v1_quote):
    data = {"customer_name":'Joe', "customer_lastName":"Bloggs",
                "customer_email":"joebloggs@gmail.com", "customer_telephone":"07949594950",
                "net":"12343", "postcode":"BT22 1ST"}
    response = v1_api.get_quote("BT22 1ST", data)
    assert response.json() == {"quoteReference":"123456789","accessProducts":[{"accessType":"Fibre","availableWithoutHardware":"false","bandwidth":"10","bearer":"100","carrier":"Level 3 Communications","hardwareOptions":[{"hardwareOption":"FCM9005 Dual Power","hardwareReference":"278316372"},{"hardwareOption":"FCM9005","hardwareReference":"278316373"}],"indicative":"false","installCharges":"0.0000","leadTime":"55","monthlyFees":"441.7800","product":"Ethernet Everywhere\xe2\x84\xa2","productReference":"278316398","secondaryOptions":[],"term":"36"}]}


# Integration test to add Customer to DB:
def test_add_customer(test_db):
    customer = add_customer("BT23 8AG", "12344", "Not Ordered", "John", "john.doe@gmail.com", "Doe", "07959469795")
    assert customer[0].net == 12344
    assert customer[1].status == "Not Ordered"
    assert customer[2].name == "John"

#Integration test for add_v1_quote
def test_add_v1_quote(test_db, mock_post_v1_quote):
    customer = add_customer("BT23 8AG", "12345", "Not Ordered", "John", "john.doe@gmail.com", "Doe", "07959469795")
    data = {"customer_name": 'Joe', "customer_lastName": "Bloggs",
            "customer_email": "joebloggs@gmail.com", "customer_telephone": "07949594950",
            "net": "12345", "postcode": "BT22 1ST"}
    response = v1_api.get_quote("BT22 1ST", data)
    add_to_db = add_v1_quote(response, customer[0], customer[1], customer[2])
    query = db.session.query(Quotation).filter(NetRef.quotation_net == "12345").first()
    assert query.net == 12345


# Integration test for NewQuote use case class.
def test_pricing_get_quote_v1(test_db, mock_post_v1_quote):
    filters = {"customer_name":'Joe', "customer_lastName":"Bloggs",
                "customer_email":"joebloggs@gmail.com", "customer_telephone":"07949594950",
                "net":"12346", "postcode":"BT22 1ST","accessTypes": [],"bandwidths":[],"btw_bandwidths":[], "btw_bw_type":[], "bearers": [], "suppliers" :["Virtual1"], "terms":[]}
    netref = pricing.run("BT23 8AG", filters, "12346", "John", "John.Doe@gmail.com", "Doe", "07959486939")
    assert netref == 12346
