from flask import Flask
from about import me
from data import mock_data
import json


app = Flask('server')


@app.get("/")
def home():
    return "Hello from flask server"


@app.get("/test")
def test():
    return "This is just a simple test"

# GET /about
# show your name


@app.get("/about")
def about_me():
    return "Mario McGrady from Alabama"


##########################################################
################ API ENDPOINTS = PRODUCTS ################
##########################################################


@app.get("/api/version")
def version():
    return "1.0"


# get /api/ about
# return first lastname
@app.get("/api/about")
def about():
    return json.dumps(me)  # parse the dict into a json string


# get /api/products
# return mock_data
@app.get("/api/products")
def get_products():
    return json.dumps(mock_data)


@app.get("/api/products/<id>")
def get_product_by_id(id):

    for prod in mock_data:
        if prod["id"] == id:
            return json.dumps(prod)


app.run(debug=True)
