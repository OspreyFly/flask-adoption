from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, ValidationError
from wtforms.validators import DataRequired, URL, NumberRange, Optional
from flask_wtf.csrf import CSRFProtect

url_validator = URL()

def validate_species(form, field):
    allowed_species = ["dog", "cat", "porcupine"]

    if field.data not in allowed_species:
        raise ValidationError("Invalid species. Choose from dog, cat, or porcupine.")

class AddPet(FlaskForm):
    """Define a form for a new pet"""
    name = StringField('Pet Name', validators=[DataRequired()])
    species = StringField('Species', validators=[DataRequired(), validate_species])
    photo_url = StringField('Photo URL', validators=[url_validator, Optional()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0,max=30)])
    notes = TextAreaField('Notes')
    available = BooleanField("Available")