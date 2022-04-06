from app.api.virtual1 import v1_api

#def test_get_quote():
#    filters = {'net': '6666', 'postcode': 'E3 4JW', 'accessTypes': ['Fibre'], 'bandwidths': ['UP_TO_10'],
#              'bearers': [], 'productGroups': [], 'suppliers': ['Level 3 Communications'], 'terms': [],
#              'csrf_token': 'ImQ1MWE5NTA1NjAzNmY0YTk1OTVmYThjNmI2ZjFiYWI3OTI0OTM4ZGEi.Ykbo2g.zKD3myNGvwOYvbMZjbn9ECTxkkk'}
#
#    test_quote = v1_api.get_quote("bt23 4jh", filters)
#
#    assert test_quote.status_code == "200"

# Create a mock API response for this test
def test_v1_quote_api():

    filters = {'net': '6666', 'postcode': 'E3 4JW', 'accessTypes': ['Fibre'], 'bandwidths': ['UP_TO_10'],
               'bearers': [], 'productGroups': [], 'suppliers': ['Level 3 Communications'], 'terms': [],
               'csrf_token': 'ImQ1MWE5NTA1NjAzNmY0YTk1OTVmYThjNmI2ZjFiYWI3OTI0OTM4ZGEi.Ykbo2g.zKD3myNGvwOYvbMZjbn9ECTxkkk'}

    result = v1_api.v1_quote_api(filters)
    assert result.status_code == 200

def test_fetch_quote():
    result = v1_api.v1_retrieve_quote_api("278200401")
    assert result.status_code == 200