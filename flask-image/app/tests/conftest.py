from app.Models.association_table import Quotation, Order, NetRef, ProviderQuote, ProviderProduct, Customer
import pytest
from app import create_app

@pytest.fixture(scope='module')
def test_quote():
    quote = Quotation('BT349Gh', '12345')
    return quote

@pytest.fixture(scope='module')
def test_provider_quote():
    provider_quote = ProviderQuote("1234567", 'Virtual 1')
    return provider_quote

@pytest.fixture(scope='module')
def test_order():
    order = Order("Not Ordered")
    return order

@pytest.fixture(scope='module')
def test_customer():
    customer = Customer("John Smith", "johnsmith@gmail.com")
    return customer


@pytest.fixture(scope='module')
def test_provider_product():
    provider_product = ProviderProduct('fibre', '100', '1000', 'BT', '250', '100.50', 'fibre everywhere', '1234567', '36', 'None')
    return provider_product


@pytest.fixture(scope='module')
def test_association():
    test_provider_pricing = ProviderQuote("Virtual1", "12345")
    test_order = Order("Not Ordered")
    test_customer = Customer("johnsmith@gmail.com", 'John Smith')
    test_provider_product = ProviderProduct('fibre', '100', '1000', 'BT', '250', '100.50', 'fibre everywhere', '1234567',
                                       '36', 'None')
    test_quote = Quotation("BT234AG", "12345")
    assoc = NetRef(test_pricing, test_quote, test_order, test_customer,test_provider_pricing, test_provider_product)
    return assoc

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('development')
    with flask_app.test_client() as test_client:
        #create application context
        with flask_app.app_context():
            yield test_client
