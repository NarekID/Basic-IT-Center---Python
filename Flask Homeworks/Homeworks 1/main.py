from flask import Flask
from flask import request
import json

app = Flask(__name__)

products = []


def add_product(data):
    global products
    found = False
    for product in products:
        if data['name'] == product['name'] and data['type'] == product['type']:
            found = True
    if not found:
        products.append(data)
        return "Product added!"
    else:
        return "Product already exists!"


@app.route("/", methods=["GET"])
def main_page():
    return "This is biggest online product shop."


@app.route("/products", methods=["GET", "POST"])
def product_list():
    global products
    if request.method == "GET":
        return str(products)
    else:
        client_json = str(request.get_json())
        if 'name' in client_json and 'type' in client_json and 'price' in client_json:
            try:
                json_data = json.loads(client_json.replace("'", '"'))
                return add_product(json_data)
            except:
                return "Wrong JSON data!"
        else:
            return "Missing data!"


app.run()
# res = requests.post("http://127.0.0.1:5000/products", json={'name' : 'bread', 'type' : 'food', 'price' : '250'})
