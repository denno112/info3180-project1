from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PropertyForm(FlaaskForm): 
# fields for property form
    title = TextAreaField('Title', validators =[InputRequired()] )

    bedrooms = TextAreaField('Number of bedrooms', validators=[
    InputRequired(), NumberRange(min=0)])
    
    bathrooms = TextAreaField('Number of bathrooms', validators=[
    InputRequired(), NumberRange(min=0)])
    
    location = TextAreaField('Location', validators=[InputRequired()])

    price = TextAreaField('Price', validators=[InputRequired()])

    pType = SelectField('Property Type', choices=[("House", "House"),("Apartment", "Apartment")])

    description = TextAreaField('Discriprion', validators =[InputRequired()])

    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only! (jpg, png)')
    ])


