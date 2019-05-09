import phonenumbers
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = "strong-secured-key"
bootstrap = Bootstrap(app)

data = []


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


@app.route("/", methods=['GET', 'POST'])
@app.route("/index/", methods=['GET', 'POST'])
def hello():
  form = NameForm()

  if form.validate_on_submit():
    data.append(form)
    return redirect("")

  return render_template('bootstrap-form.html', form=form, data=data)


if __name__ == '__main__':
  app.run(debug=True)
