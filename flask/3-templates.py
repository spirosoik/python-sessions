from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
  return '<h1>Hello Sparti Tech Lab!</h1>'


@app.route("/index/<name>")
def hello(name):
  return render_template('template-1.html', name=name)


if __name__ == '__main__':
  app.run(debug=True)
