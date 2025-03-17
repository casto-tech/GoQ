from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError, Length


def validate_name(form, field):
    """Custom validator to block specific characters in the name field."""
    blocked_chars = r"%/\<>:${}_&|#@;*()^"
    for char in blocked_chars:
        if char in field.data:
            raise ValidationError("Name cannot contain special characters.")


def validate_message(form, field):
    """Custom validator to block specific characters in the message field."""
    blocked_chars = r"/\<>:{}_|#@;*()^"
    for char in blocked_chars:
        if char in field.data:
            raise ValidationError("Message cannot contain special characters.")


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), validate_name, Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Regexp(r'^\d{10}$|^\d{3}-\d{3}-\d{4}$|^\d{7}$|^\d{3}-\d{4}$', message="Invalid phone number: Do not inlcude ( ).")])
    message = TextAreaField('Message', validators=[DataRequired(), validate_message])
