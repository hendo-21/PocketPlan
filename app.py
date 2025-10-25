from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy     # Flask-SQLAlchemy extension initialization
from sqlalchemy.orm import DeclarativeBase  # Flask-SQLAlchemy extension initialization

# Initialize the Flask-SQLAlchemy extension
class Base(DeclarativeBase):
    pass

# Gives access to db.Model class to define models, and db.session to execute queries
db = SQLAlchemy(model_class=Base)

# Creates the app
app = Flask(__name__)

# sqlite:// indicates it's a SQLite database | project.db is the name of the SQLite db file
# File location is a relative path: project.db located in same dir as app.py
app.config["SQALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

# Import database models
from . import models

# Create models and tables - update this later to a database migration tool
with app.app_context():
    db.create_all()

# Render HTML template
@app.route("/")
def index():
    return render_template('index.html')