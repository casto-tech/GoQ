from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError


def validate_name(form, field):
    """Custom validator to block specific characters in the name field."""
    blocked_chars = r"%/\<>:${\}_&|"
    for char in blocked_chars:
        if char in field.data:
            raise ValidationError(f"Name cannot contain the following characters: {blocked_chars}")


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), validate_name])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Regexp(r'^\+?\d{7,15}$', message="Invalid phone number")])
    message = TextAreaField('Message', validators=[DataRequired()])
