from flask import Flask, request
from operations import add, sub, mult, div
# Put your app in here.


app = Flask(__name__)

# http://127.0.0.1:5000/add?a=8&b=10
@app.route("/add")
def addTwoNumbers():
  """Add the a and b parameter's sum in the URL"""
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = add(a, b)
  return str(result)


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


