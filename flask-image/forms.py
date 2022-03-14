from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class NewQuote(FlaskForm):
    """Add new quote form."""
    postcode = StringField(
        'Postcode',
        [DataRequired()],
        id='postcode'
    )
    accessTypes = SelectMultipleField(
        'AccessTypes',
        choices=
        ['Any',
         'Copper',
         'Fibre',
         'FTTC'],
        id='accessType'
    )
    bandwidths = SelectMultipleField(
        'Bandwidths',
        choices=
        ['Any',
         'up to 10Mb',
         '10Mb to 100Mb',
         '100Mb to 1Gb',
         '1Gb to 10Gb'],
        id='bandwidths'
    )
    bearers = SelectMultipleField(
        'Bearers',
        choices=
        ['Any',
         '100Mb',
         '1Gb',
         '10Gb'],
        id='bandwidths'
    )
    productGroups = SelectMultipleField(
        'ProductGroups',
        choices=
        ['Any',
         'EFM',
          'EoFTTC',
          'Fibre Ethernet'],
        id='productGroups'
    )
    suppliers = SelectMultipleField(
        'Suppliers',
        choices=
        ['Any',
         'BT Wholesale',
          'Colt',
          'Level 3',
          'SSE',
          'TTB',
          'VMB',
          'Virtual1',
          'Vodafone'],
        id='suppliers'
    )
    terms = SelectMultipleField(
        'Terms',
        choices=
        ['Any',
         '12 Months',
          '36 Months'],
        id='productGroups'
    )