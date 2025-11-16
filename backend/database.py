from flask_sqlalchemy import SQLAlchemy     # Flask-SQLAlchemy extension initialization
from sqlalchemy.orm import DeclarativeBase  # Flask-SQLAlchemy extension initialization

"""
Database config:
- Initialize the Flask-SQLAlchemy extension
- Gives access to db.Model class to define models, and db.session to execute queries
"""

class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
