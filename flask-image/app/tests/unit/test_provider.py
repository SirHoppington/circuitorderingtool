from app.api.provider import BasicProvider, OAuthProvider
from app.utilities import btw_api_body

# Unit test to verify BasicProvider object initialisation
def test_basic_provider():
    basic_provider = BasicProvider("Test Provider", "https://testapi.com/",
                  "layer2-api/quoting", "layer2-api/retrieveQuote?quoteReference=",
                  "layer2-api/orderingV2", "address-lookup", "testusername", "testpassword")
    assert basic_provider.name == "Test Provider"
    assert basic_provider.url == "https://testapi.com/"
    assert basic_provider.quote_url == "layer2-api/quoting"
    assert basic_provider.retrieve_quote_url == "layer2-api/retrieveQuote?quoteReference="
    assert basic_provider.order_url == "layer2-api/orderingV2"
    assert basic_provider.address_lookup_url == "address-lookup"

# Unit test to verify OAuth Provider object initialisation
def test_oauth_provider():
    oauth_provider = OAuthProvider("Test OAuth Provider", "https://testapi.com/",
                  "layer2-api/quoting", "layer2-api/retrieveQuote?quoteReference=",
                   "layer2-api/address", "layer2-api/qual",
                  "layer2-api/orderingV2", "client_id","client_secret", "https://testapi-testa.com/oauth/accesstoken")
    assert oauth_provider.name == "Test OAuth Provider"
    assert oauth_provider.url == "https://testapi.com/"
    assert oauth_provider.quote_url == "layer2-api/quoting"
    assert oauth_provider.retrieve_quote_url == "layer2-api/retrieveQuote?quoteReference="
    assert oauth_provider.address_url == "layer2-api/address"
    assert oauth_provider.qual_url == "layer2-api/qual"
    assert oauth_provider.order_url == "layer2-api/orderingV2"
    assert oauth_provider.client_id == "client_id"
    assert oauth_provider.client_secret == "client_secret"
    assert oauth_provider.authorization_url == "https://testapi-testa.com/oauth/accesstoken"


# Unit test to confirm btw_api_body function
def test_btw_api_body():
    filters = {"customer_name":'Joe', "customer_lastName":"Bloggs",
                "customer_email":"joebloggs@gmail.com", "customer_telephone":"07949594950",
                "net":"12346", "postcode":"BT22 1ST","accessTypes": [],"bandwidths":[],"btw_bandwidths":[],
                         "btw_bw_type":[], "bearers": [], "suppliers" :["Virtual1"], "terms":[]}
    query = btw_api_body(filters, "FTTC 40:10 Mbit/s", "EtherwayGEAService")

    assert query == {"action": "add", "product": {"@type": "WholesaleEthernetElan",
                                                                    "productSpecification": {
                                                                        "id": "WholesaleEthernetElan"},
                                                                    "existingAend": "True",
                                                                    "place": [{"@type": "PostcodeSite",
                                                                               "postcode": "BT22 1ST"}], "product": [
                        {"@type": "EtherwayGEAService", "productSpecification":
                            {"id": "EtherwayGEAService"}, "bandwidth": "FTTC 40:10 Mbit/s", "resilience": "Standard"},
                        {"@type": "EtherflowDynamicService",
                         "productSpecification": {"id": "EtherflowDynamicService"}, "bandwidth": "10 Mbit/s" ,
                         "cos": "Default CoS (Standard)"}]}}