from app.queries import add_v1_quote, add_customer
from app.Models.association_table import Quotation, Order, Customer
from app.api.provider import v1_api



# Unit test Provider quote_api
def test_quote_api( mock_post_v1_quote):
    data = {"customer_name": 'Joe', "customer_lastName": "Bloggs",
            "customer_email": "joebloggs@gmail.com", "customer_telephone": "07949594950",
            "net": "12345", "postcode": "BT22 1ST"}
    response = v1_api.quote_api(data)
    assert response.json() == { "quoteReference":"123456789",
                                "accessProducts":[{"accessType":"Fibre",
                                 "availableWithoutHardware":"false","bandwidth":"10","bearer":"100",
                                                   "carrier":"Level 3 Communications","hardwareOptions":[
                                        {"hardwareOption":"FCM9005 Dual Power","hardwareReference":"278316372"},
                                        {"hardwareOption":"FCM9005","hardwareReference":"278316373"}],
                                                   "indicative":"false","installCharges":"0.0000","leadTime":"55",
                                                   "monthlyFees":"441.7800","product":"Ethernet Everywhere\xe2\x84\xa2",
                                                   "productReference":"278316398","secondaryOptions":[],"term":"36"}]}


