from flask import jsonify, request
from models import Product
from app import app, db


@app.route("/health", methods=["GET"])
def health():
    return jsonify("I am healthy!"), 200


## Create product
@app.route("/api/v1/product", methods=["POST"])
def create_product():
    try:
        data = request.json
        required_fields = ["name", "price", "image"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field {field}" }), 400
        name = data.get("name")
        price = data.get("price")
        image = data.get("image")
        new_product = Product(name=name, price=price, image=image)
        db.session.add(new_product)  
        db.session.commit()  
        return jsonify({"message": "product created successfully."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


## Get all products
@app.route("/api/v1/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    result = [product.to_json() for product in products]
    return jsonify(result), 200


## Update product
@app.route("/api/v1/product/<int:id>", methods=["PATCH"])
def update_product(id):
    try:
        product = Product.query.get(id)
        if product is None:
            return jsonify({"error": "Product not found"}), 404
        data = request.json
        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)
        product.image = data.get("image", product.image)
        db.session.commit()
        return jsonify(product.to_json())
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    

## Delete product
@app.route("/api/v1/product/<int:id>", methods=["DELETE"])
def delete_product(id):
    try:
        product = Product.query.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return jsonify({"message": "Product deleted successfully."})
        else:
            return jsonify({"error": "Product not fount"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500