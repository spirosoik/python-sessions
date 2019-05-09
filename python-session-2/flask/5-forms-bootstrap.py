from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "strong-secured-key"
bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
  name = StringField('What is your name?', validators=[DataRequired()])
  submit_btn = SubmitField('Submit Form')


@app.route("/", methods=['GET', 'POST'])
@app.route("/index/", methods=['GET', 'POST'])
def hello():
  name = None
  form = NameForm()

  if form.validate_on_submit():
    name = form.name.data
    form.name.data = ''

  return render_template('bootstrap-form.html', form=form, name=name)


if __name__ == '__main__':
  app.run(debug=True)
