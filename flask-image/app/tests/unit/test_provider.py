from app.api.provider import v1_api

def test_get_quote():
    """
    GIVEN an HTTP GET to /new_quote
    WHEN a response is received
    THEN check the response code and initial html response
    """
    v1_api.get_quote("BT23 4AJ", )
    response = test_client.get('/new_quote')
    assert response.status_code == 200
    assert b"Request New Quote" in response.data

def get_quote(self, postcode, filters):
    cleansed_form = {k: v for k, v in filters.items() if v !=
        ['Any'] and k != 'csrf_token' and k != 'postcode' and k != 'customer_email' and k != 'customer_name'}
    body = {"postcode": postcode, "filter": cleansed_form}
    response = self.quote_api(body)
    # quote_pricing = quote_to_panda_v1(response)
    # product_pricing = product_to_panda_v1(response)
    product_pricing = json_to_panda_v1(response)
    # will save all panda to database table, likely best to only save quotation reference.
    # panda.to_sql(name='provider_pricing', con=db.engine, index=False)
    return product_pricing
