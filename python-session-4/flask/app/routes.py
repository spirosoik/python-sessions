from app import app
from app import db
from app.forms import NameForm
from app.models import User
from flask import render_template, redirect


@app.route("/", methods=['GET', 'POST'])
@app.route("/index/", methods=['GET', 'POST'])
def hello():
  form = NameForm()

  if form.validate_on_submit():
    user = User()
    form.populate_obj(user)
    db.session.add(user)
    db.session.commit()
    return redirect("")

  data = User.query.all()
  return render_template('bootstrap-form.html', form=form, data=data)
