from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField,IntegerField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email, Optional,Regexp
"""
title,description, No.ofRooms|No of aBathrooms, Price|PropertyType, Location, Photo"""
class PropertyForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    description= TextAreaField('Description',validators=[DataRequired()])
    rooms=IntegerField("No. of Rooms",validators=[DataRequired()])
    #rooms=StringField("No. of Rooms",validators=[DataRequired(),Regexp("^[0-9]{1,3}",message="Invalid characters in Bedrooms. Can only contain numeric characters")])
    #bathrooms=IntegerField("No. of Bathrooms",validators=[DataRequired()])
    bathrooms=StringField("No. of Bathrooms",validators=[DataRequired(),Regexp("^[0-9]{1,3}(.5)?$",message="Invalid value for bathrooms. Can only have a whole or .5 ")])
    price=StringField("Price",validators=[DataRequired(),Regexp("^\$?([0-9]{1,3},([0-9]{3},)*[0-9]{3}|[0-9]+)(.[0-9][0-9])?$", message="Price cannot contain any non-numeric characters excluding '$',',' and '.'")])
    ptype= SelectField("Property Type", validators=[DataRequired()],choices=[('House', 'House'), ('Apartment', 'Apartment')])
    location=StringField("Location",validators=[DataRequired()])
    photo=FileField('File Upload',validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])
