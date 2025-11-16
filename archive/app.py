from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy     # Flask-SQLAlchemy extension initialization
from sqlalchemy.orm import DeclarativeBase  # Flask-SQLAlchemy extension initialization
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

"""
Database config:
- Initialize the Flask-SQLAlchemy extension
- Gives access to db.Model class to define models, and db.session to execute queries
- Create the app
- sqlite:// indicates it's a SQLite database | transactions.db is the name of the SQLite db file. File location is a relative path: project.db located in same dir as app.py
"""
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///transactions.db"
db.init_app(app)

# Define database model
class Transactions(db.Model):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[str] = mapped_column(default=date.today().strftime("%D"))
    amount: Mapped[float] = mapped_column(default=0.0)
    memo: Mapped[str] = mapped_column()

# Create models and tables - update this later to a database migration tool
with app.app_context():
    db.create_all()

# Render HTML template
@app.route("/")
def index():
    return render_template('index.html')