from app.Models.association_table import Quotation, Customer, Order, ProviderQuote, ProviderProduct


def test_new_quote(test_quote):
    """
    GIVEN a Quotation model
    WHEN a new Quotation is created
    THEN check the name and net has been asserted correctly
    """
    assert test_quote.name == ('BT349Gh' ,)
    assert test_quote.net == '12345'

def test_new_customer(test_customer):
    """
    GIVEN a Quotation model
    WHEN a new Quotation is created
    THEN check the name and net has been asserted correctly
    """
    assert test_customer.email == 'johnsmith@gmail.com'
    assert test_customer.name == ('John Smith',)

def test_new_order(test_order):
    """
    GIVEN a Quotation model
    WHEN a new Quotation is created
    THEN check the name and net has been asserted correctly
    """
    assert test_order.status == 'Not Ordered'

def test_new_provider_quote(test_provider_quote):
    """
    GIVEN a Quotation model
    WHEN a new Quotation is created
    THEN check the name and net has been asserted correctly
    """
    assert test_provider_quote.provider == 'Virtual 1'
    assert test_provider_quote.quoteReference == ('1234567' ,)

def test_new_provider_product(test_provider_product):
    """
    GIVEN a Quotation model
    WHEN a new Quotation is created
    THEN check the name and net has been asserted correctly
    """
    assert test_provider_product.accessType == ('fibre' ,)
    assert test_provider_product.bandwidth == ('100' ,)
    assert test_provider_product.bearer == ('1000' ,)
    assert test_provider_product.carrier == ('BT' ,)
    assert test_provider_product.installCharges == ('250' ,)
    assert test_provider_product.monthlyFees == ('100.50' ,)
    assert test_provider_product.product == ('fibre everywhere' ,)
    assert test_provider_product.productReference == ('1234567' ,)
    assert test_provider_product.term == ('36' ,)
    assert test_provider_product.customer_quote == 'None'

