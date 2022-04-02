from app.Models.association_table import Quotation, Order, NetRef, ProviderQuote
import pytest

@pytest.fixture(scope='module')
def test_quote():
    quote = Quotation('BT349Gh', '12345')
    return quote

@pytest.fixture(scope='module')
def test_provider_quote():
    provider_quote = ProviderQuote('Virtual1', '12345')
    return provider_quote

@pytest.fixture(scope='module')
def test_order():
    order = Order("Not Ordered")
    return order

@pytest.fixture(scope='module')
def test_association():
    test_pricing = ProviderQuote("Virtual1", "12345")
    test_order = Order("Not Ordered")
    test_quote = Quotation("BT234AG", "12345")
    assoc = NetRef(test_pricing, test_quote, test_order)
    return assoc
