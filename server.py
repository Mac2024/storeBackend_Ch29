from bson import ObjectId
from flask import Flask, request
from about import me
from data import mock_data
import random
import json
from config import db
from flask_cors import CORS


app = Flask('server')
CORS(app)  # will allow request from any origin


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
    return "Mario McGrady"


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


def fix_mongo_id(obj):
    obj['id'] = str(obj["_id"])
    del obj["_id"]
    return obj


# get /api/products
# return mock_data
@app.get("/api/products")
def get_products():
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)

    return json.dumps(mock_data)


@app.route("/api/products", methods=["POST"])
def save_product():
    product = request.get_json()

    db.products.insert_one(product)
    fix_mongo_id(product)

    return json.dumps(product)


@app.get("/api/products/<id>")
def get_product_by_id(id):
    prod = db.products.find_one({"_id": ObjectId(id)})
    if not prod:
        return "NOT FOUND"

    fix_mongo_id(prod)
    return json.dumps(prod)


# GET /api/products_category/<category>


@app.get("/api/products_category/<category>")
def get_prods_by_category(category):
    cursor = db.products.find({"category": category})
    results = []
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)

    return json.dumps(results)


# GET /api/product_cheapest
@app.get("/api/product_cheapest")
def get_cheapest():
    cursor = db.products.find({})
    solution = cursor[0]
    for prod in cursor:
        if prod["price"] < solution["price"]:
            solution = prod

    return json.dumps(solution)

    fix_mongo_id(solution)
    return json.dumps(solution)


@app.get("/api/categories")
def get_categories():
    categories = []
    cursor = db.products.find({})
    for product in cursor:
        cat = product["category"]
        if not product["category"] in categories:
            categories.append(cat)

    return json.dumps(categories)


# get return the number of prod in the catalog
# /api/count_products
@app.get("/api/count_products")
def get_products_count():
    cursor = db.products.find({})
    count = 0
    for prod in cursor:
        count + - 1

    return json.dumps({"count": count})

# get /api/search/<text>
# return all prods whose title contains text


@app.get("/api/search/<text>")
def search_products(text):
    results = []

    # do the magic here
    for prod in mock_data:
        if text in prod["title"].lower():
            results.append(prod)

    return json.dumps(results)


app.run(debug=True)
