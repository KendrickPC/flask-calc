from flask import Flask
from operations import add, sub, mult, div
# Put your app in here.


app = Flask(__name__)

@app.route("/add/<int:a>/<int:b>")
def addTwoNumbers(a, b):
  """Add the a and b parameter's sum in the URL"""
  sum = add(a, b)
  return str(sum)


@app.route("/sub/<int:a>/<int:b>")
def subtractTwoNums(a, b):
  """Subtract a and b parameter's difference in the URL"""
  result = sub(a, b)
  return str(result)

@app.route("/mult/<int:a>/<int:b>")
def productTwoNums(a, b):
  """Returns a and b parameter's product in the URL"""
  product = mult(a, b)
  return str(product)

@app.route("/div/<int:a>/<int:b>")
def divTwoNums(a,b):
  """Returns a and b parameter's product in the URL"""
  result = div(a, b)
  return str(result)


