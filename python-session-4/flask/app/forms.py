import phonenumbers

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, ValidationError


class NameForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  email = EmailField('Email address', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  phone = StringField('Phone', validators=[DataRequired()])
  submit_btn = SubmitField('Submit Form')

  def validate_phone(form, field):
    if len(field.data) > 16:
      raise ValidationError('Invalid phone number.')
    try:
      input_number = phonenumbers.parse(field.data)
      if not (phonenumbers.is_valid_number(input_number)):
        raise ValidationError('Invalid phone number.')
    except:
      input_number = phonenumbers.parse("+1" + field.data)
      if not (phonenumbers.is_valid_number(input_number)):
        raise ValidationError('Invalid phone number.')
