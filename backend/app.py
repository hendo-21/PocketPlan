from flask import Flask, request, jsonify
from database import db
from models import Transactions

"""
- Create the app
- sqlite:// indicates it's a SQLite database | transactions.db is the name of the SQLite db file. File location is a relative path: project.db located in same dir as app.py
"""
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///transactions.db"
db.init_app(app)

# Create models and tables - update this later to a database migration tool
with app.app_context():
    db.create_all()


@app.post('/transactions')
def add_transaction():
    try:
        # Get the request body
        req_body = request.get_json()

        # Create the transaction
        new_transaction = Transactions.create_transaction(req_body)

        # Return the response if successful
        return jsonify(new_transaction.to_dict()), 201
    except Exception as e:
        return {"error": str(e)}, 500


@app.get('/transactions')
def get_all_transactions():
    try:
        return jsonify(Transactions.get_all_transactions()), 200
    except Exception as e:
        return {"error": str(e)}, 500


@app.put('/transactions/<int:id>')
def update_transaction(id):
    req_body = request.get_json()
    try: 
        updated_tr = Transactions.update_transaction(id, req_body)
        if updated_tr:
            return jsonify(updated_tr.to_dict()), 200
        return {"error": "not found"}, 404
    except Exception as e:
        return {"error": str(e)}, 500


@app.delete('/transactions')
def delete_all_transactions():
    try:
        Transactions.delete_all()
        return '', 204
    except Exception as e:
        return {"error": str(e)}, 500


@app.delete('/transactions/<int:id>')
def delete_transaction(id):
    try:
        result = Transactions.delete_one(id)
        if result == 0:
            return '', 204
        return {"error": "not found"}, 404
    except Exception as e:
        return {"error": str(e)}, 500
    

@app.get('/transactions/total-spend')
def get_total_spend():
    try:
        total = Transactions.get_total_spend()
        return jsonify(total), 200
    except Exception as e:
        return {"error": str(e)}, 500
    

@app.get('/transactions/remaining')
def get_remaining():
    req_body = request.get_json()
    try:
        remaining = Transactions.get_remaining(req_body['budget'])
        return jsonify(remaining), 200
    except Exception as e:
        return {"error": str(e)}, 500