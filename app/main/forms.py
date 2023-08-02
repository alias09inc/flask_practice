from flask_wtf import FlaskForm, CSRFProtect
from wtforms import (
    Form, BooleanField, IntegerField, PasswordField, StringField,
    SubmitField, TextAreaField)

from wtforms.validators import DataRequired, EqualTo, Length, NumberRange

