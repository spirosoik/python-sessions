from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
  return '<h1>Hello Sparti Tech Lab!</h1>'


@app.route("/index/<name>")
def hello(name):
  return f'<h1>Sparti Tech Lab: hi {name}!</h1>'


if __name__ == '__main__':
  app.run(debug=True)
