# Python-Flask-CRUD
A simple Flask REST API for managing a product catalog with full CRUD functionality. Supports creating, retrieving, updating, and deleting products. Uses SQLAlchemy for database integration and includes basic error handling and a health check endpoint.

# 🛍️ Product Catalog API

A simple RESTful API built with Flask for managing a product catalog. It supports full CRUD operations and uses SQLAlchemy for database interactions.

## 🚀 Features

- Health check endpoint
- Create a new product
- Retrieve all products
- Update a product by ID
- Delete a product by ID
- Error handling for invalid requests

## 📦 Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite (or any compatible DB)

## 📁 Project Structure

- app.py # Main Flask app with API routes
- models.py # SQLAlchemy Product model
- routes.py # Contains all API endpoint routes
- requirements.txt # Python dependencies


## 📌 API Endpoints

### ✅ Health Check

- GET /health

### ➕ Create Product
- POST /api/v1/product
- Content-Type: application/json
```
{
  "name": "Product Name",
  "price": 100,
  "image": "image_url"
}
```

### 📦 Get All Products
- GET /api/v1/products

### ✏️ Update Product

- PATCH /api/v1/product/<id>
- Content-Type: application/json
```
{
  "name": "Updated Name",
  "price": 120,
  "image": "new_image_url"
}

```

### ❌ Delete Product
- DELETE /api/v1/product/<id>




## 🛠️ Setup Instructions

1. Clone the repository
```
git clone https://github.com/paras-deshbhratar/Python-Flask-CRUD.git
cd Python-Flask-CRUD

```

2. Create a virtual environment
```
python -m venv venv
On Mac: source venv/bin/activate  # On Windows: venv\Scripts\activate

```

3. Install dependencies
```
pip install -r requirements.txt

```

4. Setting Flask Env
```
# On Mac: export FLASK_APP=app.py
# On Windows: set FLASK_APP=app.py
```

5. Run the app
```
flask run

```
