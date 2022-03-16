from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class NewQuote(FlaskForm):
    """Add new quote form."""
    postcode = StringField(
        'Postcode',
        [DataRequired()],
        id='postcode'
    )
    accessTypes = MultiCheckboxField(
        'AccessTypes',
        choices=
        ['Copper',
         'Fibre',
         'FTTC'],
        id='accessType'
    )
    bandwidths = MultiCheckboxField(
        'Bandwidths',
        choices=
        [('UP_TO_10', 'up to 10Mb'),
         ('FROM_10_TO_100','10Mb to 100Mb'),
         ('FROM_100_TO_1000', '100Mb to 1Gb'),
         ('FROM_1000_TO_10000', '1Gb to 10Gb')],
        id='bandwidths'
    )
    bearers = MultiCheckboxField(
        'Bearers',
        choices=
        [('100', '100Mb'),
         ('1000', '1Gb'),
         ('10000', '10Gb')],
        id='bandwidths'
    )
    productGroups = MultiCheckboxField(
        'ProductGroups',
        choices=
        ['EFM',
          'EoFTTC',
          'Fibre Ethernet'],
        id='productGroups'
    )
    suppliers = MultiCheckboxField(
        'Suppliers',
        choices=
        [('BT Wholesale', 'BT Wholesale'),
         ('Colt', 'Colt'),
         ('Level 3 Communications', 'Level 3'),
         ('SSE Telecoms', 'SSE Telecoms'),
         ('TalkTalk Business', 'TalkTalk Business'),
         ('Virgin Media Business', 'Virgin Media Business'),
         ('Virtual1', 'Virtual1'),
         ('Vodafone', 'Vodafone')],
        id='suppliers'
    )
    terms = MultiCheckboxField(
        'Terms',
        choices=
        ['12 Months',
          '36 Months'],
        id='productGroups'
    )

class RetrieveQuote(FlaskForm):
    """Add new quote form."""
    quote_ref = StringField(
        'Quote Reference',
        [DataRequired()],
        id='quoteId'
    )
