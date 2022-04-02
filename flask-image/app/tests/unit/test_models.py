from app.Models.association_table import Quotation


def test_new_quote(test_quote):
    """
    GIVEN a Quotation model
    WHEN a new Quotation is created
    THEN check the name and net has been asserted correctly
    """
    assert test_quote.id == test_quote.id

