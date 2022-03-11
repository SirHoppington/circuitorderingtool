from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class NewQuote(FlaskForm):
    """Add new quote form."""
    postcode = StringField(
        'Postcode',
        [DataRequired()],
        id='title'
    )