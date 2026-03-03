import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from database import db
from models import Summaries, Transactions

"""
- Create the app
- static_folder points Flask at the compiled React build (frontend/dist)
- DATABASE_URL env var sets the SQLite path; defaults to local instance/transactions.db
- ALLOW_CORS env var enables CORS for local dev (Vite on :5173 → Flask on :5000)
- In production, Flask serves both the API and static files from the same origin,
  so CORS is not needed
"""
app = Flask(__name__, static_folder="../frontend/dist", static_url_path="")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///transactions.db")

if os.environ.get("ALLOW_CORS") == "true":
    CORS(app, origins=["http://localhost:5173"])
db.init_app(app)

# Create models and tables - update this later to a database migration tool
with app.app_context():
    db.create_all()
    if Summaries.query.count() == 0:
        Summaries.create_summary()


# ---- Transactions endpoints ----
@app.post('/api/transactions')
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


@app.get('/api/transactions')
def get_all_transactions():
    try:
        return jsonify(Transactions.get_all_transactions()), 200
    except Exception as e:
        return {"error": str(e)}, 500


@app.put('/api/transactions/<int:id>')
def update_transaction(id):
    req_body = request.get_json()
    try:
        updated_tr = Transactions.update_transaction(id, req_body)
        if updated_tr:
            return jsonify(updated_tr.to_dict()), 200
        return {"error": "not found"}, 404
    except Exception as e:
        return {"error": str(e)}, 500


@app.delete('/api/transactions')
def delete_all_transactions():
    try:
        Transactions.delete_all()
        return '', 204
    except Exception as e:
        return {"error": str(e)}, 500


@app.delete('/api/transactions/<int:id>')
def delete_transaction(id):
    try:
        print(type(id))
        result = Transactions.delete_one(id)
        if result == 0:
            return '', 204
        return {"error": "not found"}, 404
    except Exception as e:
        return {"error": str(e)}, 500


@app.get('/api/transactions/total-spend')
def get_total_spend():
    try:
        total = Transactions.get_total_spend()
        return jsonify(total), 200
    except Exception as e:
        return {"error": str(e)}, 500


@app.get('/api/transactions/remaining')
def get_remaining():
    req_body = request.get_json()
    try:
        remaining = Transactions.get_remaining(req_body['budget'])
        return jsonify(remaining), 200
    except Exception as e:
        return {"error": str(e)}, 500


# ---- Summaries endpoints ----
@app.post('/api/summaries')
def create_summary():
    try:
        new_summary = Summaries.create_summary()
        return jsonify(new_summary.to_dict()), 201
    except Exception as e:
        return {"error": str(e)}, 500


@app.get('/api/summaries/<int:id>')
def get_summary(id):
    try:
        summary = Summaries.get_summary(id)
        if summary:
            return jsonify(summary.to_dict()), 200
        return {"error": "not found"}, 404
    except Exception as e:
        return {"error": str(e)}, 500


@app.get('/api/summaries')
def get_all_summaries():
    try:
        return jsonify(Summaries.get_all_summaries()), 200
    except Exception as e:
        return {"error": str(e)}, 500


@app.put('/api/summaries/<int:id>')
def update_summary(id):
    req_body = request.get_json()
    try:
        updated_summary = Summaries.update_summary(id, req_body)
        if updated_summary:
            return jsonify(updated_summary.to_dict()), 200
        return {"error": "not found"}, 404
    except Exception as e:
        return {"error": str(e)}, 500


@app.delete('/api/summaries/<int:id>')
def delete_summary(id):
    try:
        result = Summaries.delete_summary(id)
        if result == 0:
            return '', 204
        return {"error": "not found"}
    except Exception as e:
        return {"error": str(e)}, 500


@app.delete('/api/summaries')
def delete_all_summaries():
    try:
        Summaries.delete_all_summaries()
        return '', 204
    except Exception as e:
        return {"error": str(e)}, 500


# ---- Static file serving ----
@app.get("/")
def serve_root():
    return send_from_directory(app.static_folder, "index.html")


@app.get("/<path:path>")
def serve_static(path):
    """
    Serves compiled React assets (JS, CSS, images) for real files in frontend/dist.
    Falls back to index.html for client-side React Router paths that have no
    corresponding file on disk.
    """
    try:
        return send_from_directory(app.static_folder, path)
    except Exception:
        return send_from_directory(app.static_folder, "index.html")
