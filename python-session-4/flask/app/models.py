from app import db


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, index=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password = db.Column(db.String(128))
  phone = db.Column(db.String(16))

  def __repr__(self):
    return '<User {}>'.format(self.name)
