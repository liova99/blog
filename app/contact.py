from flask_wtf import Form
from wtforms import (StringField, BooleanField, TextAreaField, SubmitField,
                     validators, ValidationError)

class contact_form(Form):
    name = StringField("Name", [validators.Required("Please enter your name.")])
    email = StringField("Email", [validators.Required("Please enter your email address."), validators.Email()])
    message = TextAreaField("Message", [validators.Required("Please enter a message.")])
    submit = SubmitField("Send")
