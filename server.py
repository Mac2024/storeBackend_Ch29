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
        if str(prod["id"]) == id:
            return json.dumps(prod)

    return "NOT FOUND"

# GET /api/products_category/<category>
# return all the products whose category is

# create a results list
# travel the list, get every prod
# if prod -> category is equal to the category variable
# add prod to a list
# outside the for loop, return the list as json


@app.get("/api/products_category/<category>")
def get_prods_by_category(category):
    print("your category: ", category)
    results = []
    category = category.lower()
    for prod in mock_data:
        if prod["category"].lower() == category:
            results.append(prod)

    return json.dumps(results)


# GET/api/categories
# return the list of categories
# 1 - return OK
# 2 - travel mock_data, and print the category of every product
# 3 - put the category in a list and at the end of the for loop, return the list as json

# GET /api/product_cheapest
@app.get("/api/product_cheapest")
def get_cheapest():
    solution = mock_data[0]
    for prod in mock_data:
        if prod["price"] < solution["price"]:
            solution = prod

    return json.dumps(solution)


@app.get("/api/categories")
def get_categories():
    categories = []
    for product in mock_data:
        cat = product["category"]
        if not product["category"] in categories:
            categories.append(cat)

    return json.dumps(categories)


app.run(debug=True)
