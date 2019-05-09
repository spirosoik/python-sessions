from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/lala")
def index():
  return '<h1>Alli selid</h1>'


@app.route("/index/<name>")
def hello(name):
  return render_template('bootstrap.html', name=name)


if __name__ == '__main__':
  app.run(debug=True)
