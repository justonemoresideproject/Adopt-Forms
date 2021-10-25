from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class PetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('dog', 'Dog'), ('cat', 'Cat'), ('porcupine', 'Porcupine')])
    photo_url = StringField('Photo URL')
    age = IntegerField('Age')
    notes = StringField('Notes')
    is_available = BooleanField('Available', default=True)
