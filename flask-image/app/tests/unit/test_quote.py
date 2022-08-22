from app.api.provider import v1_api
from app.Quote.quote import pricing

#Integration test for V1 Provider API get_quote() function
def test_v1_quote(mock_post_v1_quote):
    data = {"customer_name":'Joe', "customer_lastName":"Bloggs",
                "customer_email":"joebloggs@gmail.com", "customer_telephone":"07949594950",
                "net":"12345", "postcode":"BT22 1ST"}
    response = v1_api.get_quote("BT22 1ST", data)
    assert response.json() == {"quoteReference":"123456789","accessProducts":[{"accessType":"Fibre","availableWithoutHardware":"false","bandwidth":"10","bearer":"100","carrier":"Level 3 Communications","hardwareOptions":[{"hardwareOption":"FCM9005 Dual Power","hardwareReference":"278316372"},{"hardwareOption":"FCM9005","hardwareReference":"278316373"}],"indicative":"false","installCharges":"0.0000","leadTime":"55","monthlyFees":"441.7800","product":"Ethernet Everywhere\xe2\x84\xa2","productReference":"278316398","secondaryOptions":[],"term":"36"}]}

# Integration test for NewQuote use  case class.
def test_pricing_get_quote_v1(test_db, mock_post_v1_quote):
    filters = {"customer_name":'Joe', "customer_lastName":"Bloggs",
                "customer_email":"joebloggs@gmail.com", "customer_telephone":"07949594950",
                "net":"12345", "postcode":"BT22 1ST","accessTypes": [],"bandwidths":[],"btw_bandwidths":[], "btw_bw_type":[], "bearers": [], "suppliers" :["Virtual1"], "terms":[]}
    netref = pricing.run("BT23 8AG", filters, "12345", "John", "John.Doe@gmail.com", "Doe", "07959486939")
    assert netref == 12345