# 10/26/25 - Leaving this in repo for now, but will delete later. Just one model needed so leaving model definition in main app file. Addresses circular import issue.

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from app import db

class Budget(db.Model):
    # Set the name of the table
    __tablename__ = "budget"

    # Create column for unique ID - needed/highly recommended
    id: Mapped[int] = mapped_column(primary_key=True)

    # Create columns for settings, defaulting to $0 
    budget: Mapped[int] = mapped_column(default=0)
    spent: Mapped[int] = mapped_column(default=0)
    remaining: Mapped[int] = mapped_column(default=0)