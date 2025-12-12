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
    print("Request Body:", req_body)
    try: 
        tr_to_update = db.get_or_404(Transactions, id, description="Transaction not found")
        print("Transaction:", tr_to_update)
        if 'date' in req_body:
            tr_to_update.date = req_body['date']
        if 'amount' in req_body:
            tr_to_update.amount = req_body['amount']
        if 'memo' in req_body:
            tr_to_update.memo = req_body['memo']
        db.session.commit()
        return jsonify(tr_to_update.to_dict()), 200
    except Exception as e:
        return {"error": str(e)}, 404


@app.delete('/transactions')
def delete_all_transactions():
    try:
        db.session.query(Transactions).delete()
        db.session.commit()
        return '', 204
    except Exception as e:
        return {"error": str(e)}, 500


@app.delete('/transactions/<int:id>')
def delete_transaction(id):
    try:
        to_delete = db.get_or_404(Transactions, id, description="Transaction not found")
        db.session.delete(to_delete)
        db.session.commit()
        return '', 204
    except Exception as e:
        return {"error": str(e)}, 404