from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, PasswordField

from wtforms import validators, ValidationError, BooleanField


class UserAddForm(Form):
    username = StringField("Username", [validators.Length(min=4, max=20)])
    password = PasswordField("Password", validators.DataRequired(),
                             validators.EqualTo('confirm', message="Passwords must be equal."))
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)', [validators.Required()])


